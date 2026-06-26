import os


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""


def scan_project(project_path):

    project = {
        "kotlin_files": [],
        "java_files": [],
        "xml_files": [],
        "gradle_files": [],
        "manifest": "",
        "toml": "",
        "files": []
    }

    for root, dirs, files in os.walk(project_path):

        # Ignore build folders
        dirs[:] = [
            d for d in dirs
            if d not in [
                "build",
                ".gradle",
                ".idea",
                ".git"
            ]
        ]

        for file in files:

            full_path = os.path.join(root, file)

            # ----------------------------
            # Kotlin
            # ----------------------------
            if file.endswith(".kt"):

                content = read_file(full_path)

                project["kotlin_files"].append(full_path)

                project["files"].append({
                    "name": file,
                    "path": full_path,
                    "type": "kotlin",
                    "content": content
                })

            # ----------------------------
            # Java
            # ----------------------------
            elif file.endswith(".java"):

                content = read_file(full_path)

                project["java_files"].append(full_path)

                project["files"].append({
                    "name": file,
                    "path": full_path,
                    "type": "java",
                    "content": content
                })

            # ----------------------------
            # XML
            # ----------------------------
            elif file.endswith(".xml"):

                content = read_file(full_path)

                project["xml_files"].append(full_path)

                project["files"].append({
                    "name": file,
                    "path": full_path,
                    "type": "xml",
                    "content": content
                })

                if file == "AndroidManifest.xml":
                    project["manifest"] = content

            # ----------------------------
            # Gradle
            # ----------------------------
            elif file == "build.gradle" or file == "build.gradle.kts":

                content = read_file(full_path)

                project["gradle_files"].append(content)

            # ----------------------------
            # Version Catalog
            # ----------------------------
            elif file == "libs.versions.toml":

                project["toml"] = read_file(full_path)

    return project