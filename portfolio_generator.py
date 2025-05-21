import os
import PySimpleGUI as sg

def generate_portfolio(name, bio, projects):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{name}'s Portfolio</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary-color: #1e90ff;
                --bg-color: #f9f9f9;
                --card-color: white;
                --text-color: #333;
            }}
            body {{
                font-family: 'Inter', sans-serif;
                background-color: var(--bg-color);
                color: var(--text-color);
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 900px;
                margin: auto;
            }}
            h1 {{
                color: var(--primary-color);
                text-align: center;
            }}
            h2 {{
                border-bottom: 2px solid var(--primary-color);
                padding-bottom: 5px;
                margin-top: 40px;
            }}
            .project-card {{
                background: var(--card-color);
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                transition: transform 0.2s;
            }}
            .project-card:hover {{
                transform: scale(1.01);
            }}
            a {{
                color: var(--primary-color);
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{name}'s Portfolio</h1>
            <h2>About Me</h2>
            <p>{bio}</p>
            <h2>Projects</h2>
    """

    for project in projects:
        html += f"""
            <div class="project-card">
                <h3>{project['title']}</h3>
                <p>{project['description']}</p>
                <a href="{project['link']}" target="_blank">View Project</a>
            </div>
        """

    html += """
        </div>
    </body>
    </html>
    """

    with open("portfolio.html", "w", encoding="utf-8") as f:
        f.write(html)

# --- GUI Layout ---
sg.theme("LightBlue2")
layout = [
    [sg.Text("Your Name:"), sg.InputText(key="-NAME-")],
    [sg.Text("Your Bio:"), sg.Multiline(key="-BIO-", size=(50, 5))],
    [sg.Text("Projects (Enter 1 per line: title|description|link):")],
    [sg.Multiline(key="-PROJECTS-", size=(70, 8))],
    [sg.Button("Generate Portfolio"), sg.Button("Exit")]
]

window = sg.Window("Portfolio Website Generator", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    if event == "Generate Portfolio":
        name = values["-NAME-"].strip()
        bio = values["-BIO-"].strip()
        raw_projects = values["-PROJECTS-"].strip().splitlines()

        projects = []
        for line in raw_projects:
            parts = line.split("|")
            if len(parts) == 3:
                projects.append({"title": parts[0].strip(), "description": parts[1].strip(), "link": parts[2].strip()})

        if name and bio and projects:
            generate_portfolio(name, bio, projects)
            sg.popup("✅ Portfolio generated as 'portfolio.html'")
        else:
            sg.popup_error("Please fill in all fields correctly.")

window.close()
