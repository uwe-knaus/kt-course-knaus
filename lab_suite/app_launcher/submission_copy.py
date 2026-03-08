"""
Submission-Copy: Kopiert Dateien aus dem Task-Ordner (oder assignments/) nach submissions/,
falls dort noch nicht vorhanden. EDIT/STARTEN arbeiten dann mit der Kopie (keine Merge-Konflikte).
"""
from __future__ import annotations

import shutil
from pathlib import Path

# lab_suite = Parent von app_launcher
_MODULE_DIR = Path(__file__).resolve().parent
LABS_DIR = _MODULE_DIR.parent / "labs"

# Dozent legt diese Datei im Lab-Ordner ab; beim nächsten Launcher-Aufruf (Studierenden-Modus)
# werden alle Task-Dateien nach submissions/ überschrieben, danach wird die Datei gelöscht.
ONE_TIME_UPDATE_FILENAME = "one_time_update.txt"


def ensure_submission_copy(
    folder_name: str,
    filename: str,
    source_subdir: str | None = None,
    force_overwrite: bool = False,
) -> Path | None:
    """
    Stellt sicher, dass eine Kopie der Datei in submissions/ existiert.
    Wenn submissions/<filename> fehlt (oder force_overwrite=True), wird von
    <task_folder>/<source_subdir>/<filename> bzw. <task_folder>/<filename> kopiert.

    Args:
        folder_name: Lab-Ordner (z. B. 01_02_Informationstheorie).
        filename: Dateiname (z. B. entropy1.py, user_template.py).
        source_subdir: Optionaler Unterordner im Task (z. B. "assignments").
            Wenn None, liegt die Quelle direkt im Task-Ordner.
        force_overwrite: Wenn True, bestehende Datei in submissions/ überschreiben.

    Returns:
        Pfad zur Datei in submissions/ (absolut), oder None wenn die Quelldatei nicht existiert.
    """
    task_dir = LABS_DIR / folder_name
    submissions_dir = task_dir / "submissions"
    dest = submissions_dir / filename

    if source_subdir:
        source = task_dir / source_subdir / filename
    else:
        source = task_dir / filename

    if not source.is_file():
        return None

    submissions_dir.mkdir(parents=True, exist_ok=True)

    if force_overwrite or not dest.exists():
        shutil.copy2(source, dest)

    return dest.resolve()


def _top_level_script_names(task_dir: Path) -> list[str]:
    """.py- und .ipynb-Dateien direkt im Task-Ordner (wie in scan.py)."""
    names = []
    for f in task_dir.iterdir():
        if not f.is_file():
            continue
        if f.suffix not in (".py", ".ipynb"):
            continue
        if f.name.startswith("__"):
            continue
        names.append(f.name)
    return sorted(names)


def ensure_all_task_script_copies(
    folder_name: str,
    force_overwrite: bool = False,
) -> list[Path]:
    """
    Kopiert alle .py- und .ipynb-Dateien der obersten Ebene aus dem Task-Ordner
    nach submissions/, falls sie dort noch fehlen (oder bei force_overwrite=True).

    Returns:
        Liste der Pfade in submissions/, die (neu oder bereits vorhanden) existieren.
    """
    task_dir = LABS_DIR / folder_name
    if not task_dir.is_dir():
        return []
    result = []
    for name in _top_level_script_names(task_dir):
        path = ensure_submission_copy(
            folder_name, name, force_overwrite=force_overwrite
        )
        if path is not None:
            result.append(path)
    return result


def ensure_app_submission_files(
    folder_name: str,
    force_overwrite: bool = False,
) -> list[Path]:
    """
    Kopiert assignments/user_template.py und user_callbacks.py nach submissions/,
    falls sie im Task-Ordner existieren und in submissions/ fehlen (oder force_overwrite=True).

    Returns:
        Liste der Pfade in submissions/ (die nun existieren).
    """
    result = []
    for name in ("user_template.py", "user_callbacks.py"):
        path = ensure_submission_copy(
            folder_name, name, source_subdir="assignments", force_overwrite=force_overwrite
        )
        if path is not None:
            result.append(path)
    return result


def ensure_sidedata_copy(
    folder_name: str,
    force_overwrite: bool = False,
) -> bool:
    """
    Kopiert den Ordner task/sidedata/ nach submissions/sidedata/, falls er im Task existiert.
    Ohne force_overwrite: nur Dateien kopieren, die in submissions/sidedata/ noch fehlen.
    Mit force_overwrite: alle Dateien kopieren und bestehende überschreiben.
    Wird nur im Studenten-Modus aufgerufen; im Instructor-Modus (.instructor_key) nicht.

    Returns:
        True, wenn sidedata existierte und ggf. kopiert wurde; False, wenn task/sidedata/ nicht existiert.
    """
    task_dir = LABS_DIR / folder_name
    source_dir = task_dir / "sidedata"
    if not source_dir.is_dir():
        return False
    submissions_dir = task_dir / "submissions"
    dest_dir = submissions_dir / "sidedata"
    dest_dir.mkdir(parents=True, exist_ok=True)
    for src_file in source_dir.rglob("*"):
        if not src_file.is_file():
            continue
        rel = src_file.relative_to(source_dir)
        dest_file = dest_dir / rel
        if force_overwrite or not dest_file.exists():
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, dest_file)
    return True


def run_force_refresh_if_requested(folder_name: str) -> bool:
    """
    Prüft, ob im Lab-Ordner one_time_update.txt existiert (vom Dozenten gesetzt).
    Falls ja: kopiert alle .py/.ipynb, assignments-Dateien und sidedata/ nach
    submissions/ mit Überschreiben, löscht one_time_update.txt und gibt True zurück.
    Andernfalls: keine Aktion, Rückgabe False.

    Nur im Studenten-Modus relevant; wird von app.py vor den ensure_*-Aufrufen aufgerufen.
    """
    task_dir = LABS_DIR / folder_name
    flag_path = task_dir / ONE_TIME_UPDATE_FILENAME
    if not flag_path.is_file():
        return False
    ensure_all_task_script_copies(folder_name, force_overwrite=True)
    ensure_app_submission_files(folder_name, force_overwrite=True)
    ensure_sidedata_copy(folder_name, force_overwrite=True)
    flag_path.unlink(missing_ok=True)
    return True
