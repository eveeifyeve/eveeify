import re

def extract_and_replace(text: str, replacements: dict[str, str]) -> str:
    # Regular expression to find content inside ${}
    pattern = r'\$\{([^}]+)\}'

    def replacer(match_items) -> str:
        key = match_items.group(1)
        return replacements.get(key, match_items.group(0))  # Return the replacement if found, else return the original match

    # Substitute the placeholders with the replacements
    result = re.sub(pattern, replacer, text)
    return result

def turn_list_to_img(skills: list[str]) -> str:
    base_url = "https://go-skill-icons.vercel.app/api/icons?i="
    skills_str = ",".join(skills)
    img_url = f"{base_url}{skills_str}&perline=13"

    html_snippet = f"""
<p align="center">
    <a href="https://github.com/LelouchFR/skill-icons">
        <img src="{img_url}" />
    </a>
</p>
    """
    return html_snippet

def detials_template(summary: str, input: str) -> str:
    html_snipet = f"""
<details>
    <summary>{summary}✍️</summary>
    {input}
</details>
"""
    return html_snipet

def githubStats(url_point: str, params: list, alt: str) -> str:
    username = "eveeifyeve"
    base_url = "https://github-readme-stats.vercel.app/api"

    # Construct the parameters string
    params_str = "&".join(params)

    return f"""
    <img src="{base_url}{url_point}?username={username}{params_str}" height="150" alt="{alt} graph"/>
    """

try:
    # Open the file and read its contents
    with open('README.md.rst', 'r') as file:
        template = file.read()


    # Skills
    lang_skils = [
            "ts", 
            "react", 
            "html",
            "css",
            "astro", 
            "go", 
            "kotlin", 
            "lua", 
            "rust", 
            "zig", 
            "cpp", 
            "sass", 
            "vue", 
            "java", 
            "swift", 
            "svg",
            "nix", 
            "gleam",
            "python",
            ]

    tool_skils = [
            "maven",
            "gradle",
            "bootstrap",
            "godot",
            "nextjs",
            "supabase",
            "replit",
            "tailwind",
            "tauri",
            "electron",
            "vercel",
            "vite",
            "webpack",
            "prisma",
            "gatsby",
            "nginx",
            "nodejs",
            "cmake",
            "githubactions",
            "flutter",
            "jquery",
            "angular",
            "solidjs",
            "bun",
            ]

    db_skils = [
            "mongodb",
            "sqlite",
            "postgresql",
            "surrealdb",
            ]

    other_skils = [
            "vim",
            "vscode",
            "docker",
            "postman",
            "github",
            "gimp",
            "pr",
            ]

    skills = lang_skils + tool_skils + db_skils + other_skils

    skillsImg = turn_list_to_img(skills)

    # Details 
    stats_base_url = "https://github-readme-stats.vercel.app/api"

    stats = f"""
<img src="{stats_base_url}?username=eveeifyeve&bg_color=30,34e8ff,9e26ff&title_color=000&text_color=fff" height="150" alt="stats graph"/>
<img src="{stats_base_url}/top-langs?username=eveeifyeve&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&bg_color=30,34e8ff,9e26ff&hide_border=false&order=2&title_color=000&text_color=fff" height="150" alt="languages graph"  />
    """

    major = {
            "TeaClient": "CEO/Founder",
            "OpusClient": "Developer (2023-2024)"
            }

    opensource = {
            "Evolutify": "CEO",
            "Cordevall": "CEO",
            "Minecraft-essentials": "Owner"
            }

    major_projects_lines = [f"- {project}: {role}" for project, role in major.items()]
    opensource_projects_lines = [f"- {project}: {role}" for project, role in opensource.items()]

    roles = f"""
Major Projects/Company’s
{',\n'.join(major_projects_lines)},

Opensource Projects: 
{',\n'.join(opensource_projects_lines)}
    """

    details = detials_template("Github Stats ⚡️", stats) + detials_template("Roles ✍️", roles)

    replacements = {
            "List": skillsImg,
            "Details": details,
            }

    result = extract_and_replace(template, replacements)

    with open("README.md", "w") as readme:
        readme.write(result)

except FileNotFoundError:
    print("Error: The file 'test.txt' was not found.")
except IOError as e:
    print(f"Error reading the file: {e}")
