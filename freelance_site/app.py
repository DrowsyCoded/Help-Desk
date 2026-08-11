from flask import Flask, render_template

app = Flask(__name__)

SERVICES = [
    {
        "name": "Web Design",
        "blurb": "Custom websites for small businesses, built and launched end to end.",
        "price": "Custom quote",
        "turnaround": "Scoped per project",
        "features": ["Full design, build, and launch", "Mobile-responsive from the start", "Direct collaboration, start to finish"],
        "link": "https://www.fiverr.com/jonathonjhunt/design-and-build-a-custom-small-business-website",
    },
    {
        "name": "ATS Resume + LinkedIn",
        "blurb": "Resume and LinkedIn rewrites built to pass applicant tracking systems.",
        "price": "From $45",
        "turnaround": "3–5 day delivery",
        "features": ["ATS-optimized resume rewrite", "Full LinkedIn profile overhaul on higher tiers", "1–unlimited revision rounds by tier"],
        "link": "https://www.fiverr.com/jonathonjhunt/rewrite-your-resume-and-linkedin-profile-to-be-ats-friendly",
    },
    {
        "name": "SEO Blog & Article Writing",
        "blurb": "Optimized blog posts and articles written to rank and hold attention.",
        "price": "From $35",
        "turnaround": "Per-article, fast turnaround",
        "features": ["Keyword-researched topics", "SEO-structured, ready to publish", "Single articles or multi-article packs"],
        "link": "https://www.fiverr.com/jonathonjhunt/write-seo-optimized-blog-posts-and-articles",
    },
    {
        "name": "Cover Letters",
        "blurb": "Cover letters tailored to a specific job, not a recycled template.",
        "price": "From $25",
        "turnaround": "Fast turnaround",
        "features": ["Written for the specific job posting", "Matches the voice of your resume", "Not a recycled template"],
        "link": "https://www.fiverr.com/jonathonjhunt",
    },
]

SERVICE_FAQ = [
    {
        "q": "How do revisions work?",
        "a": "Each service includes a set number of revision rounds, more on higher tiers. We go back and forth within that scope until it's right.",
    },
    {
        "q": "Do you guarantee results?",
        "a": "No. I don't promise a specific outcome like an interview, a ranking, or a sale — nobody honestly can. What I guarantee is a professional, tested deliverable built around what you actually asked for.",
    },
    {
        "q": "How do we communicate?",
        "a": "Everything is async — messages, drafts, and revisions handled by email or message. No scheduled calls required.",
    },
    {
        "q": "Why is web design a custom quote and not a fixed price?",
        "a": "Every site is different in scope. Web design gets a quote after a quick conversation about what you actually need; everything else has a real starting price up front.",
    },
]

PORTFOLIO = [
    {
        "name": "Help Desk Ticket Tracker",
        "tag": "Full-stack web app",
        "blurb": "A Flask/SQLite help desk system with ticket CRUD, dashboards, CSV export, "
                 "a JSON API, and private per-ticket messaging links.",
        "link": "/tracker",
        "link_label": "Live demo",
        "secondary_link": "https://github.com/DrowsyCoded/Help-Desk",
        "secondary_label": "Source on GitHub",
    },
    {
        "name": "Butcher Bob's",
        "tag": "Website mockup",
        "blurb": "A homepage redesign built for a family butcher shop open since 1988, "
                 "matching their existing branding and product lines.",
        "link": None,
        "link_label": None,
    },
    {
        "name": "Hoosier Honey Farm",
        "tag": "Website redesign — in progress",
        "blurb": "An in-progress redesign for a bee rescue apiary, staying inside their "
                 "existing free platform to fit their budget.",
        "link": None,
        "link_label": None,
    },
]


BLOG_POSTS = [
    {
        "slug": "how-to-beat-an-ats-resume-2026",
        "title": "How to Beat an ATS: What Actually Gets Your Resume Read in 2026",
        "description": "What applicant tracking systems actually check for, the formatting mistakes that get resumes auto-rejected, and what really improves your odds.",
        "date": "August 11, 2026",
        "read_time": "7 min read",
        "excerpt": "Applicant tracking systems reject resumes for reasons that have nothing to do with your qualifications. Here's what actually trips them up — and what genuinely helps.",
        "body": """
<p>Most advice about "beating the ATS" treats it like one piece of software with one set of
rules. It isn't. There are dozens of applicant tracking systems in use, and they don't all work
the same way. But some things hold true across almost all of them. Here's what's real, and what's
just internet folklore.</p>

<h2>How These Systems Work</h2>
<p>I write resumes for a living, and the number of good candidates I see get filtered out for
reasons that have nothing to do with their actual qualifications is honestly kind of maddening.
An ATS doesn't "reject" you the way people imagine. Most of them parse your resume into fields
(name, contact info, work history, skills) and make that searchable for a recruiter, sometimes
with a keyword-match score attached. The danger isn't a robot judging your career. It's a robot
misreading your resume so badly that a real person never sees it, or a recruiter searching for
a term your resume never says out loud.</p>

<h2>Formatting Mistakes That Hurt You</h2>
<ul>
<li><strong>Tables and multi-column layouts.</strong> Many parsers read left-to-right, top-to-bottom.
A two-column resume can get scrambled into nonsense order that has nothing to do with how it looks to you.</li>
<li><strong>Text inside headers, footers, or graphics.</strong> Contact info or job titles placed
in a header/footer or embedded in an image are frequently skipped entirely.</li>
<li><strong>Non-standard section titles.</strong> "Where I've Been" instead of "Work Experience"
might read fine to a human and confuse a parser looking for standard headings.</li>
<li><strong>Fancy fonts and symbols.</strong> Decorative bullet icons or unusual characters can
turn into garbled text on the other end.</li>
</ul>
<p>None of this means your resume has to look boring. It means the underlying structure needs
to be simple, even if the visual design isn't.</p>

<h2>What Genuinely Helps</h2>
<ul>
<li><strong>Match the job posting's language.</strong> If the posting says "project management,"
and your resume says "managed projects," say it their way too. Keyword search is often literal.</li>
<li><strong>Use standard section headers.</strong> Work Experience, Education, Skills. Predictable
beats clever here.</li>
<li><strong>Submit the file type they ask for.</strong> If a posting specifies .docx, don't send a
design-heavy PDF assuming it's fine. Some systems still parse Word files more reliably.</li>
<li><strong>Quantify what you can.</strong> Numbers don't move the ATS score directly, but they make
the resume stronger for the human who reads it next, and that's the actual goal.</li>
</ul>

<h2>What Doesn't Matter</h2>
<p>You'll see claims that certain fonts are "ATS-approved" or that keyword-stuffing a white-text
section at the bottom of your resume tricks the system. Most modern parsers strip formatting
before reading text anyway, and stuffing invisible keywords is exactly the kind of thing that
looks bad if a human ever does see the raw file. Simple, honest, and well-structured beats
clever tricks.</p>

<h2>The Real Takeaway</h2>
<p>There's no single ATS to "beat," so nobody can honestly guarantee a pass, including me. What
you can do is remove the unforced errors: bad formatting, missing keywords, and vague
descriptions that make a strong candidate look generic on paper. That's what genuinely moves
the needle, and it's the same thing a human recruiter responds to once your resume clears the
software.</p>
""",
    },
    {
        "slug": "how-much-does-a-small-business-website-cost",
        "image": "blog-website-cost-cover.jpg",
        "title": "How Much Does a Small Business Website Actually Cost in 2026?",
        "description": "A straight answer on small business website pricing — DIY builders, freelancers, and agencies — plus the costs that show up after launch.",
        "date": "August 11, 2026",
        "read_time": "6 min read",
        "excerpt": "DIY builder, freelancer, or agency — the real price range for a small business site, what actually drives the cost, and what shows up on the bill after launch.",
        "body": """
<p>I get asked this constantly, and the honest answer is always "it depends," which is a
frustrating thing to hear when you just want a number. If you've started looking into getting
a website built, you've probably noticed the answers are all over the place: $200 on one forum,
$15,000 on an agency's pricing page. Both can be true. Here's what actually determines where
you land, and what most quotes don't tell you up front.</p>

<h2>The Short Answer</h2>
<p>For a real small business site — not a single-page placeholder — expect somewhere between
<strong>$500 and $3,000</strong> if you're hiring a freelancer or small independent designer,
<strong>$3,000 to $15,000+</strong> for an agency, or <strong>$0 to $30/month</strong> if you build
it yourself on a platform like Squarespace or Wix. None of those numbers are wrong. They're
just answering different questions.</p>

<h2>What Drives the Price</h2>
<p>The number you get isn't random. A handful of factors move it more than anything else:</p>
<ul>
<li><strong>Custom design vs. a template.</strong> A themed template someone else can also buy
is cheaper than a layout designed around your actual brand and content.</li>
<li><strong>Page count and complexity.</strong> A five-page site is a different job than a
full catalog, booking system, or e-commerce store.</li>
<li><strong>Who writes the content.</strong> Design-only quotes assume you're handing over
finished copy. If you need someone to write it too, that's separate work.</li>
<li><strong>Ongoing changes.</strong> A static site you'll rarely touch costs less to build than
one you expect to update weekly.</li>
</ul>

<h2>What This Actually Looks Like</h2>
<p>Numbers in the abstract don't mean much, so here are three realistic scenarios based on the
kind of work that actually comes through the door:</p>
<ul>
<li><strong>A five-page site for a local bakery or barbershop.</strong> Homepage, about, services
or menu, gallery, contact form. No booking system, no e-commerce, content mostly provided by the
owner. This is squarely freelancer territory: <strong>$600–$1,200</strong>, or free to about
$20/month if the owner builds it themselves on a platform.</li>
<li><strong>An eight-to-ten-page site with content written from scratch.</strong> Same structure as
above, but the business needs someone to actually write the copy, not just plug in what they hand
over, plus a blog section for SEO. That extra writing work pushes it to
<strong>$1,500–$3,000</strong> with a freelancer, since it's design and copywriting combined.</li>
<li><strong>A site with online ordering, booking, or a product catalog.</strong> Once you add real
functionality, custom logic, and testing, you're past what most freelancers price casually and
into <strong>$3,000–$8,000+</strong> territory, often agency work, sometimes a freelancer who
specializes in that kind of build.</li>
</ul>
<p>The pattern holds across all three: pages and content are what push the price up, not the
platform or who's building it.</p>

<h2>Costs Beyond the Build</h2>
<p>The build price is rarely the whole story. Budget for these too, regardless of who builds
your site:</p>
<ul>
<li><strong>Domain name</strong> — roughly $10–$20/year</li>
<li><strong>Hosting</strong> — free to a few dollars a month on a platform, more for custom-built
sites on dedicated hosting</li>
<li><strong>Maintenance</strong> — someone needs to keep it updated and working, whether that's
you, a platform's built-in tools, or a developer on retainer</li>
</ul>
<p>A cheap build with no plan for these becomes an expensive surprise six months in.</p>

<h2>What I Charge, And Why</h2>
<p>I don't publish a flat price for web design, and I'm upfront about why: a five-page
informational site and a site with online ordering aren't the same job. Pretending they cost
the same isn't honest pricing, it's a bait-and-switch waiting to happen. What I do instead is
talk through what you actually need first, then give you a real number based on that scope,
not a guess.</p>

<h2>Bottom Line</h2>
<p>If a quote feels too good to be true for the scope you're describing, it usually is. Corners
get cut somewhere, whether that's design quality, revisions, or what happens after launch. The
real question isn't "what's the cheapest option" but "what does this business actually need to
look credible and work correctly," and pricing from there.</p>
""",
    },
]

PROCESS_STEPS = [
    {"num": "01", "name": "Discovery", "blurb": "We talk through what your business actually needs before anything gets built."},
    {"num": "02", "name": "Draft", "blurb": "I design, write, or build a first version for you to react to."},
    {"num": "03", "name": "Revise", "blurb": "We refine it together until it's right — not just approved."},
    {"num": "04", "name": "Deliver", "blurb": "You get the final site, files, or published content, ready to use."},
]


@app.route("/")
def home():
    return render_template("home.html", services=SERVICES, portfolio=PORTFOLIO, active="home")


@app.route("/about")
def about():
    return render_template("about.html", active="about")


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES, process=PROCESS_STEPS, faq=SERVICE_FAQ, active="services")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", portfolio=PORTFOLIO, active="portfolio")


@app.route("/blog")
def blog():
    return render_template("blog.html", posts=BLOG_POSTS, active="blog")


@app.route("/blog/<slug>")
def blog_post(slug):
    post = next((p for p in BLOG_POSTS if p["slug"] == slug), None)
    if post is None:
        return render_template("blog.html", posts=BLOG_POSTS, active="blog"), 404
    return render_template("blog_post.html", post=post, active="blog")


@app.route("/contact")
def contact():
    return render_template("contact.html", active="contact")


if __name__ == "__main__":
    app.run(debug=True, port=5050)
