import os
import shutil
import re

# 1. Copy images
src_dir = 'c:/Users/marya/OneDrive/Desktop/KNES 381'
dest_dir = 'c:/Users/marya/OneDrive/Documents/mary_annenc.github.io/images'
headshot_src = os.path.join(src_dir, 'IMG_6299.JPG')
banner_src = os.path.join(src_dir, 'c5c43d5b-23c2-4963-aebc-d85907bb135e.JPG')

headshot_dest = os.path.join(dest_dir, 'headshot.jpg')
banner_dest = os.path.join(dest_dir, 'club_banner.jpg')

if os.path.exists(headshot_src):
    shutil.copy2(headshot_src, headshot_dest)
if os.path.exists(banner_src):
    shutil.copy2(banner_src, banner_dest)

# 2. Read index.html
html_path = 'c:/Users/marya/OneDrive/Documents/mary_annenc.github.io/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    base_html = f.read()

# Extract blocks
post_about_pattern = r'<!-- Post -->.*?<article class="box post post-excerpt">.*?<h2><a href="#">About Me</a></h2>.*?</article>'
post_exp_pattern = r'<!-- Post -->.*?<article class="box post post-excerpt">.*?<h2><a href="#">Experience &amp; Projects</a></h2>.*?</article>'

post_about_match = re.search(post_about_pattern, base_html, re.DOTALL)
post_exp_match = re.search(post_exp_pattern, base_html, re.DOTALL)

post_about_html = post_about_match.group(0) if post_about_match else ""
post_exp_html = post_exp_match.group(0) if post_exp_match else ""

# Create replacement post for contact
post_contact_html = '''<!-- Post -->
						<article class="box post post-excerpt">
							<header>
								<h2><a href="#">Contact & Resume</a></h2>
								<p>Let's Get in Touch</p>
							</header>
							<div class="info">
								<span class="date"><span class="month">Apr<span>il</span></span> <span class="day">14</span><span class="year">, 2026</span></span>
							</div>
							<p>
								<strong>Connecting professionally</strong> is something I look forward to. Whether it's to discuss medicine, community building, or potential opportunities, feel free to reach out.
							</p>
							<p>
								<strong>Email:</strong> <a href="mailto:chukwunyemmaryanne@gmail.com">chukwunyemmaryanne@gmail.com</a><br/>
								<strong>LinkedIn:</strong> <a href="#">[Profile Link Add Later]</a>
							</p>
							<p>
								<strong>Resume / CV Download:</strong> <br/>
								<a href="cv.pdf" class="button">Download My CV</a>
							</p>
						</article>'''

def build_page(page_name, active_tab, core_content):
    # Base setup
    html = base_html
    # Remove original posts together
    html = re.sub(post_about_pattern, "###CORE_CONTENT_PLACEHOLDER###", html, flags=re.DOTALL)
    html = re.sub(post_exp_pattern, "", html, flags=re.DOTALL)
    html = html.replace("###CORE_CONTENT_PLACEHOLDER###", core_content)
    
    # Update Nav
    nav_original = '''				<!-- Nav -->
					<nav id="nav">
						<ul>
							<li class="current"><a href="#">About Me</a></li>
							<li><a href="#">Experience &amp; Projects</a></li>
							<li><a href="#">Contact</a></li>
						</ul>
					</nav>'''
					
    nav_new = '''				<!-- Nav -->
					<nav id="nav">
						<ul>
							<li ''' + ('class="current"' if active_tab == 'about' else '') + '''><a href="index.html">About Me</a></li>
							<li ''' + ('class="current"' if active_tab == 'experience' else '') + '''><a href="experience.html">Experience &amp; Projects</a></li>
							<li ''' + ('class="current"' if active_tab == 'contact' else '') + '''><a href="contact.html">Contact</a></li>
						</ul>
					</nav>'''
    
    html = html.replace(nav_original, nav_new)
    return html

# Page modifications
about_html = build_page('index', 'about', post_about_html)
about_html = about_html.replace('images/pic01.jpg', 'images/headshot.jpg')

exp_html = build_page('experience', 'experience', post_exp_html)
exp_html = exp_html.replace('images/pic02.jpg', 'images/club_banner.jpg')

contact_html = build_page('contact', 'contact', post_contact_html)

# Write pages
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(about_html)

with open('c:/Users/marya/OneDrive/Documents/mary_annenc.github.io/experience.html', 'w', encoding='utf-8') as f:
    f.write(exp_html)

with open('c:/Users/marya/OneDrive/Documents/mary_annenc.github.io/contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

# 3. Apply Pastel CSS
css_path = 'c:/Users/marya/OneDrive/Documents/mary_annenc.github.io/assets/css/main.css'
css_append = '''

/* --- Custom Pastel Theme Overrides --- */
body, body.is-preload, html {
    background-color: #fcf9f5 !important;
    background-image: none !important;
}

#sidebar {
    background-color: #e8f0f2 !important;
    border-right: 1px solid #d8e3e7 !important;
}

#logo {
    background-color: #a7c5eb !important;
    background-image: none !important;
}

#logo a {
    color: #ffffff !important;
}

#nav > ul > li.current > a {
    background-color: #ffd1dc !important;
    color: #fff !important;
}

#nav > ul > li > a:hover {
    background-color: #ffe4e1 !important;
    color: #555 !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #7d8b99 !important;
}

a {
    color: #a7c5eb !important;
}

.box.post {
    background: #ffffff !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03) !important;
    border: none !important;
    padding: 30px !important;
}

.box.recent-posts {
    background-color: #fef0f2 !important; 
    border-radius: 10px !important;
    border: none !important;
}
.box.recent-comments {
    background-color: #effcf1 !important; 
    border-radius: 10px !important;
    border: none !important;
}
.box.text-style1 {
    background-color: #fdf5ea !important; 
    border-radius: 10px !important;
    border: none !important;
}

.button {
    background-color: #ffd1dc !important;
    color: white !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
    border: none !important;
}
.button:hover {
    background-color: #ffb6c1 !important;
}
'''
with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_append)
