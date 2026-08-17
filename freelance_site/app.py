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
        "name": "Screen Notes AI",
        "tag": "Desktop app",
        "blurb": "A local desktop app that listens to whatever's playing on your screen, "
                 "transcribes it in real time with Whisper, and organizes it into topic-grouped "
                 "notes using a local Qwen model. Nothing leaves the machine.",
        "link": None,
        "link_label": None,
    },
    {
        "name": "Family Butcher Shop",
        "tag": "Website mockup",
        "blurb": "A full homepage redesign mockup for a family-owned butcher shop open since "
                 "1988, built to match their existing color palette and branding, real product "
                 "lines, and store details, delivered as a ready-to-view design before any "
                 "platform changes were made.",
        "link": None,
        "link_label": None,
    },
    {
        "name": "Bee Rescue Apiary",
        "tag": "Website redesign",
        "blurb": "A full redesign of a bee rescue apiary's existing Google Sites page, "
                 "covering the homepage, shop, and educational content, staying on their "
                 "existing free platform and iterated with the client before touching the "
                 "live site.",
        "link": None,
        "link_label": None,
    },
    {
        "name": "Faith-Based Lifestyle Brand",
        "tag": "Shopify copywriting — in progress",
        "blurb": "A homepage and product description rewrite for a Shopify store selling "
                 "faith-based digital products, alongside an image audit flagging AI-generated "
                 "and mismatched photography with real replacement recommendations.",
        "link": None,
        "link_label": None,
    },
]


BLOG_POSTS = [
    {
        "slug": "how-to-beat-an-ats-resume-2026",
        "icon": "resume",
        "title": "How to Beat an ATS: What Actually Gets Your Resume Read in 2026",
        "description": "What applicant tracking systems actually check for, the formatting mistakes that get resumes auto-rejected, and what really improves your odds.",
        "date": "August 10, 2026",
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
        "icon": "cost",
        "title": "How Much Does a Small Business Website Actually Cost in 2026?",
        "description": "A straight answer on small business website pricing — DIY builders, freelancers, and agencies — plus the costs that show up after launch.",
        "date": "August 10, 2026",
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
    {
        "slug": "why-your-small-business-isnt-showing-up-on-google",
        "icon": "seo",
        "title": "Why Your Small Business Isn't Showing Up on Google",
        "description": "The real reasons small business websites don't show up in local search, and the fundamentals that actually move the needle, from your Google Business Profile to reviews to page speed.",
        "date": "August 11, 2026",
        "read_time": "5 min read",
        "excerpt": "Having a website doesn't mean people can find it. Here's what actually determines whether your business shows up when someone searches, and why rebuilding the site usually isn't the first fix.",
        "body": """
<p>A lot of small business owners assume having a website means people can find it. That's not really
how it works. I've had more than one client tell me their site has been live for two years and
they've never gotten a single customer from it. Almost every time, the problem isn't the website
itself. It's that Google has no reason to think the site matters yet.</p>

<h2>Start With Your Google Business Profile, Not Your Website</h2>
<p>If you search for a plumber or a bakery near you, most of what shows up isn't website rankings,
it's the map pack, those three listings with a star rating and a phone number. That comes from your
Google Business Profile, which is free and separate from your website. If you haven't claimed and
filled that out completely, hours, categories, photos, service area, that's the first thing to fix,
before anything else.</p>

<h2>Reviews Matter More Than People Expect</h2>
<p>A business with 40 reviews and a 4.6 star average will usually beat a business with zero reviews
and a technically better website. It's not just a trust signal for customers, it's one of the
stronger local ranking factors Google uses. If you've never asked happy customers to leave a
review, that's free ground you're giving up.</p>

<h2>Your Website Still Needs the Basics Covered</h2>
<p>Once the profile and reviews are in place, the website itself needs to actually say what you do
and where you do it. That sounds obvious, but I see sites that never mention the city or region
they serve anywhere in the text, just in a logo or a footer address. If your homepage doesn't say
"we're a landscaping company serving Medford and the Rogue Valley," Google has less reason to
connect you with someone searching for exactly that.</p>

<h2>Speed and Mobile Aren't Optional Anymore</h2>
<p>Most local searches happen on a phone, in the car, standing in a parking lot. If your site takes
eight seconds to load or the text is too small to read without zooming, people leave, and Google
notices that too. This is one of the most common issues I find on older small business sites,
especially ones built years ago on outdated platforms.</p>

<h2>The Honest Timeline</h2>
<p>None of this happens overnight. Local SEO is closer to compounding interest than a light switch,
small consistent improvements add up over months, not days. Anyone who promises page one rankings
in a week is selling something. What actually works is getting the fundamentals right and staying
consistent, the profile, the reviews, the on-page basics, and giving it time to build.</p>

<p>If your business has a website that isn't bringing in customers, it's worth a real look at whether
these basics are actually in place before assuming the site needs to be rebuilt from scratch.</p>
""",
    },
    {
        "slug": "is-your-website-using-ai-generated-stock-photos",
        "icon": "eye",
        "title": "Is Your Website Using AI-Generated Stock Photos? Here's How Customers Can Tell",
        "description": "How to spot AI-generated and generic stock photography on a small business website, why it quietly costs you customer trust, and what to use instead.",
        "date": "August 12, 2026",
        "read_time": "6 min read",
        "excerpt": "Most visitors can't say why a photo feels off, but they notice. Here's what actually gives away an AI-generated or mismatched stock image, and what I replaced my own site's with.",
        "body": """
<p>I spent part of this week going through a client's website image by image, flagging which
photos looked genuine and which ones looked generated. It's become a bigger part of my process
than I expected, because it turns out a lot of small business sites have this problem, including,
until a few days ago, mine. Three blog covers on this exact site were AI-generated images of a
room that doesn't exist. I'll get to what I replaced them with, but first, the tells.</p>

<h2>What Actually Gives It Away</h2>
<p>Most visitors won't consciously clock a photo as AI-generated. They'll just feel a little less
sure about the business, without knowing why. But if you look closely, the signs are usually
there:</p>
<ul>
<li><strong>Hands doing something specific.</strong> Writing, holding a tool, gesturing mid-conversation.
This is still where generators struggle most: fingers that grip an object at an impossible angle,
a pen that seems to merge into the hand instead of resting in it.</li>
<li><strong>Lighting that's too even.</strong> Real firelight, lamp light, and sunset light are
directional and a little messy. Generated "golden hour" scenes tend to glow evenly across every
face in the frame, like the light source is coming from everywhere at once.</li>
<li><strong>A scene that's a little too on-the-nose.</strong> A cash jar labeled "mission" next to a
globe. A hoodie-wearing man journaling in perfect side-lighting. When a photo illustrates a concept
that literally, it's usually because someone typed that concept into a prompt box.</li>
<li><strong>The same photo, doing double duty.</strong> If a business's "About" page and a client
testimonial section use the exact same generic desk-and-coffee-cup photo, neither one was taken
for that business specifically.</li>
<li><strong>Backgrounds that don't quite hold together.</strong> Bookshelves with no readable titles,
picture frames with no actual picture in them, text on a screen or sign that dissolves into
nonsense the moment you really look at it.</li>
</ul>

<h2>Why It Costs You Trust</h2>
<p>None of this is really about the technology. It's about what a fake photo tells a visitor about
the business behind it. If your whole pitch is that you're real, personal, and hands-on, and the
first thing someone sees is a stock image of a stranger who was never actually in your shop, on
your job site, or in your kitchen, the message and the image are working against each other. People
don't need to identify the photo as AI to feel that mismatch. They just trust the page a little
less, and move on a little faster.</p>

<h2>A Real Example: My Own Site</h2>
<p>I built this site's blog section with cover images generated the same way a lot of small
businesses end up doing it: a quick AI image prompt, a nice-looking result, done. They looked
fine individually. But once I started actually training myself to spot this stuff for client work,
I couldn't unsee it on my own homepage. So this week I pulled all three and rebuilt the covers from
scratch, no photo at all. Each one is now a simple card built from the site's own design system:
the same dark background, the same gold accent line, a small line-icon relevant to the post, and
the headline. It took less effort than generating a new image would have, it'll never look
subtly wrong to a sharp-eyed visitor, and it can't drift out of style the way a photo trend can.</p>

<h2>What To Use Instead</h2>
<p>You don't need a professional photographer to fix this. In order of what actually helps most:</p>
<ul>
<li><strong>A real photo, even an imperfect one.</strong> A phone photo of your actual workspace,
product, or storefront will beat a polished fake every time. Slightly imperfect reads as honest.</li>
<li><strong>Stock photography chosen for the specific context, not the general vibe.</strong> If
you're going to use stock, pick an image that actually matches what the page is describing, not
just one that looks nice in the slot. And don't reuse the same photo across five different pages.</li>
<li><strong>No photo at all.</strong> A clean design element, a simple icon, or just strong
typography on your own brand colors is more honest than a fake photo trying to fill a blank space.
That's the option I ended up using here.</li>
</ul>

<h2>Bottom Line</h2>
<p>A website's images are doing a job whether you think about them or not: telling a visitor whether
this is a real business or a template with a name attached. If you're not sure whether your own
site's photos are helping that case or quietly working against it, that's exactly the kind of gap
I look for when I audit a client's site, and it's worth checking before you assume the problem is
somewhere else entirely.</p>
""",
    },
    {
        "slug": "how-to-write-product-descriptions-that-sound-like-you",
        "icon": "pencil",
        "title": "How to Write Product Descriptions That Sound Like You, Not a Template",
        "description": "Why most ecommerce product descriptions read the same, where a founder's real voice actually lives, and a practical process for writing copy that sounds like a person instead of a template.",
        "date": "August 13, 2026",
        "read_time": "11 min read",
        "excerpt": "Most product pages read like they were written by whoever was available that day, not the person who actually built the thing. Here's where the real voice is hiding, how to find it, and how to write descriptions that rank and still sound like a person.",
        "body": """
<p>I rewrote a full set of product descriptions this week for a client, and the biggest thing I
learned had nothing to do with the products themselves. It's that almost nobody writes their own
product descriptions in their own voice, even when they're the one who built the thing being sold.
They default to the same flat, feature-list tone every other store uses, because that's what
"product description" sounds like in their head. It doesn't have to, and honestly, it shouldn't.
A product description is one of the only pieces of copy on your entire site where a customer is
actively deciding whether to hand you their money, and most businesses waste that moment on
language that could belong to anyone.</p>

<h2>Why Most Product Descriptions Sound the Same</h2>
<p>Open ten random product pages and you'll notice the pattern fast: a bolded feature, a short
benefit clause, repeat. "Premium quality materials." "Perfect for everyday use." "Built to last."
None of it is wrong exactly, it's just interchangeable. You could swap the product name on half
of these descriptions and nothing would feel off. That's the actual problem. Not bad grammar, not
typos, just a total absence of anyone specific behind the words.</p>
<p>Part of this comes from how most people learn to write product copy in the first place. They
look at a competitor's page, borrow the structure, and fill in their own features. Feature,
benefit, feature, benefit. It's not a bad instinct, structure matters, but structure isn't the
same thing as voice, and copying someone else's structure usually means copying their tone along
with it. The result is a whole category of ecommerce writing that reads like it was generated by
a formula, because functionally, it was.</p>

<h2>What "Voice" Actually Means in a Product Description</h2>
<p>"Voice" gets thrown around a lot in marketing without much of a definition, so here's mine: it's
the specific, slightly imperfect way a real person would explain this product if you asked them
about it directly. Not their brand's mission statement. Not their elevator pitch. The way they'd
actually talk about it, including the small opinions and details that a template would never
include, like which feature they're personally proudest of, or the one thing customers keep
asking about.</p>
<p>Voice is what makes a description feel like it was written by someone who has actually held the
product in their hands, not researched it. That distinction is usually obvious to a reader within
the first sentence, even if they couldn't explain why.</p>

<h2>Where the Real Voice Actually Lives</h2>
<p>The client I mentioned had this exact problem: generic copy on a site that was otherwise doing
fine. When I asked a handful of direct questions (what made you build this, which product are you
proudest of, what does a customer usually tell you after they buy it), the answers were sharper
and more specific than anything already on the site. He'd also put together a free guide for his
own customers at some point, and that document had more voice in one paragraph than the entire
product catalog combined. The real writing was already out there. It just hadn't made it onto the
product pages yet.</p>
<p>This is true almost every time. A founder's actual voice is usually sitting somewhere already:
an email reply, a lead magnet, a video transcript, a text they sent a customer once, not because
they're hiding it, but because nobody thought to go looking for it before writing new copy from
scratch. Before you write a single new word for a product page, it's worth doing an inventory of
everywhere that voice might already exist.</p>

<h2>A Practical Process for Writing in Your Own Voice</h2>
<ul>
<li><strong>Mine what already exists.</strong> Before writing a single new sentence, read
anything the business owner has already written in their own words: about pages, email replies,
social captions, a PDF guide, anything. Pull actual phrases, not just ideas. If a sentence from an
email reply is better than anything you could write from scratch, use it.</li>
<li><strong>Ask questions a customer would actually ask.</strong> Not "tell me about your
brand," that gets a rehearsed answer. Ask which product they're proudest of, what a real customer
said after buying, what almost stopped them from making the thing at all. Specific questions get
specific, usable answers. Vague questions get marketing-speak.</li>
<li><strong>Keep the specific, cut the generic.</strong> If a sentence could describe a
competitor's product just as easily, it's not doing its job. Replace it with something only true
of this product, made by this person. This is the single biggest edit that separates a generic
description from a real one.</li>
<li><strong>Write it like you'd say it out loud.</strong> If a business owner wouldn't actually
say a sentence to a customer standing in front of them, it probably doesn't belong on the page
either. Read every draft out loud before calling it finished. Anything that sounds stiff on the
way out of your mouth reads stiff on the page too.</li>
<li><strong>Leave in a little roughness.</strong> Perfectly polished copy can read as fake in the
same way an overly smooth stock photo does. A slightly blunt sentence, an honest admission, or a
specific number instead of a rounded-off one all signal that a real person wrote this.</li>
</ul>

<h2>The Questions I Actually Ask</h2>
<p>When I'm working through a product catalog for a client, I don't ask open-ended branding
questions. I ask questions built to surface something specific and usable. A few that consistently
work:</p>
<ul>
<li>What made you build this particular product, specifically?</li>
<li>Which product are you proudest of, and why that one over the others?</li>
<li>What's something a customer has told you after using it that stuck with you?</li>
<li>What almost stopped you from making this at all?</li>
<li>If someone's on the fence about buying this, what would you actually say to them?</li>
</ul>
<p>None of these questions ask someone to describe their brand. They ask for a specific memory or
opinion, and specific answers are what turn into good copy.</p>

<h2>SEO Without Sounding Like SEO</h2>
<p>You can still lead a description with the phrase a customer would actually type into Google,
you just don't have to make it sound like you're talking to Google instead of a person. A line
like "a daily prayer devotional for dads who want to lead their family in faith" covers real
search intent and still reads like a sentence a human wrote, because it is one. Keyword-stuffing
and authentic copy aren't actually opposites. The trick is writing the search phrase the way a
real person would say it, not the way a spreadsheet would.</p>
<p>A simple way to find that phrase: think about what a friend would text you if they were asking
where to find this exact product. That's usually closer to real search language than anything a
keyword tool spits out first. Google's own autocomplete and "People also ask" boxes are also worth
checking, they're a free window into how real customers phrase the exact problem your product
solves.</p>

<h2>Common Mistakes That Undo Good Product Copy</h2>
<ul>
<li><strong>Leading with specs instead of the person.</strong> Dimensions and materials matter,
but they belong after the reason someone would want this, not before it.</li>
<li><strong>Writing every product the same length.</strong> A flagship product usually deserves
more than a simple accessory. Forcing every description into the same word count flattens the
ones that actually need room to breathe.</li>
<li><strong>Reusing the same adjectives across the whole catalog.</strong> If "amazing," "premium,"
and "perfect" show up on every single product page, none of them mean anything by the third one.</li>
<li><strong>Never revisiting old copy.</strong> A description written when a business launched
often no longer reflects what the founder has learned since. Voice, like the business itself,
changes over time.</li>
</ul>

<h2>How Long Should a Product Description Actually Be?</h2>
<p>There's no universal number, and anyone who gives you one is guessing. What actually determines
length is how much a customer needs to know before they feel confident buying. A $15 accessory
might only need two honest sentences. A $200 workbook or a piece of furniture usually needs more:
what it solves, who it's for, what's included, and why this version is different from the cheaper
alternative sitting one tab over. Write until the real questions are answered, then stop. Padding
a short, honest description out to hit a word count almost always makes it worse, not better.</p>

<h2>Bottom Line</h2>
<p>A product description's job is to sound like the person who made the thing, not like a
template with the product name swapped in. If your own product pages feel like they could belong
to any store, the fix usually isn't a rewrite from scratch, it's going back to find the voice
that's already sitting in your own words somewhere, and building the copy around that instead.
That's the same process I use for every client's catalog, mine what's already real, ask better
questions, and cut anything that could belong to someone else.</p>
""",
    },
    {
        "slug": "seo-basics-for-small-business-websites",
        "icon": "chart",
        "title": "SEO Basics Every Small Business Website Needs",
        "description": "A plain-language guide to on-page SEO fundamentals for small business websites: title tags, headers, URL structure, content, site speed, internal links, and a realistic timeline for results.",
        "date": "August 13, 2026",
        "read_time": "13 min read",
        "excerpt": "Your Google Business Profile gets you found on the map. Your actual website still needs its own SEO fundamentals in place, or none of that traffic converts once it lands. Here's what actually matters, and how to check your own site in ten minutes.",
        "body": """
<p>A client called me a few months back convinced his website was broken. Traffic had flatlined,
new inquiries had dried up, and he was ready to pay for a full rebuild. The site wasn't broken.
It loaded fine, looked decent, had real products on it. But every single page shared the exact
same page title ("Home"), there wasn't a single H1 tag anywhere on the site, and the URLs were a
string of random numbers his old website builder had generated automatically. Google had no real
idea what any individual page was actually about, so it had nothing to rank. That's not a rebuild
problem. That's an SEO fundamentals problem, and it's one of the most common things I run into on
small business sites that otherwise look completely fine.</p>
<p>I've written before about <a href="/blog/why-your-small-business-isnt-showing-up-on-google">why a lot of small businesses aren't showing up on Google</a>, and most
of that comes down to the Google Business Profile, reviews, and the basics Google uses to rank
local results. This post is the other half of that. Once someone actually lands on your website,
a separate set of fundamentals takes over: the actual on-page SEO of the site itself. This is the
part people skip because it sounds technical. Most of it isn't. Here's what actually matters, in
plain language, and a way to check your own site against it in about ten minutes.</p>

<h2>What SEO Actually Is, Without the Jargon</h2>
<p>Strip away the acronyms and SEO is just making it easy for both Google and an actual human to
understand what a page is about and whether it answers their question. That's the whole concept.
Everything else, keywords, meta tags, headers, backlinks, is just the mechanics of doing that
clearly and consistently across a site. If you keep that one definition in mind, almost every SEO
decision gets a lot easier to make, because you can just ask: does this make the page clearer, or
murkier?</p>

<h2>Title Tags and Meta Descriptions</h2>
<p>The title tag is the blue link text in a Google search result, and it's one of the strongest
signals on the entire page for both ranking and getting someone to actually click. A vague title
like "Home" or "Welcome to Our Website", the exact mistake my client's site was making on every
single page, wastes that space entirely and gives Google nothing to distinguish one page from
another. A better title says what the page is and where, something like "Custom Cabinets in
Medford, Oregon | Riverside Woodworks." Specific, includes what you do, includes where.</p>
<p>Every page on a site needs its own unique title. If your about page, your homepage, and your
services page all say the same thing, you've told Google those pages are interchangeable, and
it'll treat them that way in results.</p>
<p>The meta description is the paragraph underneath the title in search results. It doesn't
directly affect ranking much anymore, but it's still your pitch for the click, so write it like
ad copy, not a summary. One or two sentences on what a visitor gets and why this page instead of
a competitor's.</p>

<h2>Headers and Page Structure</h2>
<p>Every page should have exactly one H1, and it should describe what the page is about in plain
language, not a clever tagline. Everything under it uses H2s and H3s to break the page into
scannable sections, the same way a well-organized document uses headings. This isn't just for
Google, it's for the visitor who's skimming the page in four seconds to decide if it's worth
reading further. A wall of unbroken text loses both.</p>

<h2>URL Structure</h2>
<p>A URL like <code>yoursite.com/p?id=4471&cat=9</code> tells a search engine and a human
nothing. A URL like <code>yoursite.com/products/cedar-planters</code> tells both exactly what's
there before the page even loads. Keep URLs short, readable, and built from real words, not
auto-generated IDs.</p>

<h2>Content and Keyword Use, Without Stuffing</h2>
<p>Write the way a customer would actually search, not the way a brochure would describe the
business. If people search "emergency plumber Medford Oregon," a page that only ever says
"residential plumbing solutions" is missing an easy match. The fix isn't repeating the exact
phrase five times, it's using the words a real customer would use, naturally, in the first couple
sentences and a header or two. One clear match beats ten forced ones.</p>

<h2>Site Speed and Mobile Friendliness</h2>
<p>Most local searches happen on a phone, often while someone's already moving toward a decision.
If a page takes eight seconds to load or the text is too small to read without zooming, most
people leave before they ever see what you offer, and Google notices that drop-off too. This is
one of the most common issues on older small business sites, especially ones built years ago on
platforms that were never optimized for mobile in the first place.</p>

<h2>Internal Linking</h2>
<p>Link between your own pages when it makes sense: a blog post about cabinet care linking to the
cabinets product page, a services page linking to a relevant past project. This does two things:
it helps a visitor find more of what they're looking for, and it helps Google understand which
pages on your site are most important by how often they're linked to internally.</p>

<h2>Backlinks, Briefly</h2>
<p>A backlink is another website linking to yours, and it's still one of the stronger ranking
signals that exists. For most small businesses, the realistic path to this isn't a big campaign,
it's local: getting listed in your city's business directory, a mention from a supplier or
partner, a local news writeup, a guest post on a related local blog. A handful of genuine local
links does more than a hundred low-quality ones from nowhere in particular.</p>

<h2>A Realistic Timeline</h2>
<p>None of this moves overnight. Google needs to recrawl and reassess a page, and that process
typically plays out over weeks and months, not days. Anyone promising page one rankings in a week
is selling something. What actually works is getting these fundamentals right once, keeping them
consistent as you add pages, and letting the compounding effect build over time.</p>

<h2>Common SEO Myths That Waste Your Time</h2>
<p>A few things I hear constantly that just aren't true anymore, or never were:</p>
<ul>
<li><strong>"I need to submit my site to Google."</strong> You don't. Google finds and crawls
new sites on its own within days, usually, as long as nothing is actively blocking it.</li>
<li><strong>"More keywords is always better."</strong> Repeating a phrase unnaturally reads badly
to visitors and can actually work against you. One clear, natural mention beats ten forced ones.</li>
<li><strong>"SEO is a one-time project."</strong> Rankings aren't permanent. A site that hasn't
been touched in three years while competitors keep publishing will slowly lose ground even if
nothing about it "broke."</li>
<li><strong>"Paying for backlinks works."</strong> Buying links from low-quality link farms is one
of the few things that can actively get a site penalized. It's not a shortcut, it's a risk.</li>
</ul>

<h2>A 10-Minute Self-Audit You Can Do Right Now</h2>
<p>Open your own website and check these five things before assuming you need to hire anyone:</p>
<ul>
<li>Open three different pages and look at the browser tab text. Is every single one identical,
or does each say something specific about that page?</li>
<li>Right-click any page and view the page source (or just look for the big, bold heading text).
Is there exactly one clear H1, or none at all?</li>
<li>Look at your URLs. Do they read like <code>/services/kitchen-remodel</code>, or like a string
of random numbers and letters?</li>
<li>Pull up your site on your phone using mobile data, not wifi. Does it load in a couple of
seconds, and is the text readable without pinching to zoom?</li>
<li>Read your homepage's first paragraph out loud. Does it say what you do and where, in plain
words a customer would actually type into Google?</li>
</ul>
<p>If you found even one real problem in that list, that's usually the highest-leverage fix
available, higher than a full redesign, and often something that can be corrected in an
afternoon rather than a rebuild.</p>

<h2>Bottom Line</h2>
<p>My client's "broken" website didn't need a rebuild. It needed unique titles, one clear H1 per
page, real words in the URLs, and content written the way his actual customers searched, not the
way his old builder had auto-generated things years earlier. None of that requires a specialized
SEO tool or a monthly retainer to get right the first time. A clear title tag, proper page
structure, and a site that loads fast on a phone will put a small business ahead of most of its
local competitors, who are still skipping these exact same basics.</p>
""",
    },
    {
        "slug": "5-signs-your-website-is-costing-you-customers",
        "icon": "warning",
        "title": "5 Signs Your Website Is Costing You Customers",
        "description": "The quiet website problems that drive customers away before they ever call or email you — and how to tell if yours has them.",
        "date": "August 14, 2026",
        "read_time": "9 min read",
        "excerpt": "A website doesn't have to be broken to lose you business. Here are the five most common problems I find on small business sites — and how to check for them yourself in five minutes.",
        "body": """
<p>Here's a scenario I run into a lot. A business owner tells me their website is \"fine.\" It's
up, it looks reasonably put-together, nobody's complained about it. But when I ask how many
leads or calls it's actually brought in this month, the honest answer is usually \"I'm not sure\"
or \"not many.\" A website can be online, functional, and still be quietly losing you customers
every single day, because most people who leave don't tell you why. They just leave. No error
message, no complaint, no bounce notification. They land on the page, decide within a few
seconds that this isn't the business they're calling, and close the tab.</p>
<p>The good news is that the problems behind this are almost always the same handful of things,
and most of them take five minutes to check for yourself. Here are the five I see most often,
what they actually cost you, and how to tell if your site has them.</p>

<h2>1. It Loads Too Slowly</h2>
<p>Speed is one of the least glamorous parts of a website and one of the most expensive to get
wrong. Google's own research into mobile page speed has found that as load time stretches from
one second to three seconds, the odds of a visitor bouncing before the page even finishes
loading rise sharply, and it keeps climbing the longer the wait goes on. People aren't being
impatient for no reason. On a phone, on the go, a slow site reads as a warning sign: if the
website is this neglected, is the business behind it any better?</p>
<p>The usual causes are predictable: oversized images that were never compressed before upload,
too many third-party scripts and plugins running in the background (chat widgets, tracking
pixels, font libraries), and cheap or oversold hosting that chokes under real traffic. None of
these are hard to fix once you know they're there. The problem is that most site owners never
know, because the site loads fine for them, sitting at their desk on fast home wifi, which is
nothing like the experience of a customer standing in a parking lot on 4G.</p>
<p><strong>How to check:</strong> Run your homepage through Google's PageSpeed Insights
(pagespeed.web.dev) and look at the mobile score specifically, not desktop. If it's flagging
large images or excessive load time, that's not a cosmetic issue, that's customers leaving
before they see what you offer.</p>

<h2>2. It Doesn't Actually Work on a Phone</h2>
<p>\"Mobile-friendly\" gets thrown around as a checkbox, but there's a real difference between a
site that technically resizes on a phone and one that's actually built to be used on one. I
still regularly pull up small business sites on my phone and find text too small to read without
zooming, buttons packed so close together that I tap the wrong one, or a navigation menu that
opens and then won't close. Most web traffic for local, service-based businesses now comes from
a phone, not a desktop. If the mobile experience is an afterthought, you're making the majority
of your visitors work the hardest to become customers.</p>
<p>This one is sneaky because it's invisible to the owner if they mostly check their own site on
a laptop. The fix isn't always a full rebuild either. Sometimes it's genuinely small: bigger tap
targets, a simplified mobile menu, a phone number that's an actual tappable link instead of
plain text someone has to copy by hand.</p>
<p><strong>How to check:</strong> Pull up your own site on your phone, on cellular data, not wifi,
and try to do the thing a customer would actually do: find your hours, get your phone number, or
fill out a contact form. If any of that is annoying for you, it's more annoying for someone who
doesn't already know your business.</p>

<h2>3. The Information Is Out of Date</h2>
<p>This is the one that costs real, specific customers, not just a vague drop in traffic. Old
hours listed after they changed. A phone number that used to work. A \"current\" promotion from
two years ago still pinned to the homepage. A staff or services page that doesn't mention what
you actually offer now. I've seen small business sites where the copyright year in the footer
was the most recently updated thing on the entire page.</p>
<p>Stale information doesn't just fail to help, it actively misleads. Someone who shows up during
listed hours and finds the doors locked, or who calls a disconnected number, doesn't usually try
again. They assume the business closed and move to the next search result. The website is
supposed to be the most reliable source of truth about your business. When it's wrong, it's
worse than having no website at all, because at least an absence of information doesn't send
someone confidently to the wrong place.</p>
<p><strong>How to check:</strong> Read your own site like a stranger would, top to bottom, and
fact-check every claim against what's actually true today: hours, prices, services, contact
info, any \"current\" offers. If anything's stale, that's an easy fix with a real payoff.</p>

<h2>4. There's No Clear Next Step</h2>
<p>A surprising number of small business websites look good and still don't tell a visitor what
to do. They describe the business, list some services, maybe show a gallery, and then just
stop. There's no obvious button to call, book, request a quote, or get in touch. The contact
information is buried on a separate page, or worse, exists but isn't a clickable link. A visitor
who's already interested still has to hunt for how to become a customer, and a lot of people
simply won't do that hunting. They'll go find a competitor whose site makes the next step
obvious.</p>
<p>This is less about design flair and more about not making a visitor think. Every page on your
site should answer, without effort, \"okay, so what do I do now?\" A visible phone number,
a direct \"Book Now\" or \"Get a Quote\" button, a short contact form near the top of the page,
not just tucked at the bottom. Small, unglamorous changes, but they're often the single biggest
lever on how many visitors actually turn into inquiries.</p>
<p><strong>How to check:</strong> Land on your homepage as if you'd never seen it before and time
how long it takes you to find your phone number or a way to contact you. If it takes more than a
few seconds, or requires clicking to another page, that's friction you're paying for.</p>

<h2>5. It Looks Unfinished or Untrustworthy</h2>
<p>This is the hardest one to self-diagnose, because you already trust your own business. A
first-time visitor doesn't have that context yet, and they're reading small signals to decide
whether you're legitimate. Broken images. Placeholder text that was never replaced (\"Lorem
ipsum\" or \"Insert business name here\" left in by accident). Generic stock photos that clearly
aren't your actual shop, team, or product. Dead links that go nowhere. A design that hasn't been
touched since the site launched years ago, with visual conventions that quietly signal \"this
business might not be around anymore\" even when it very much is.</p>
<p>None of these individually sinks a business. Together, they add up to an impression, and
first-time visitors form that impression in seconds, long before they read a word of your
copy. It's the same instinct that makes you hesitate before walking into a physical store with
a flickering sign and a dusty window display. A website is that storefront now, for better or
worse, for most people's first impression of you.</p>
<p><strong>How to check:</strong> Ask someone outside your business, a friend, a family member,
someone who's never seen the site, to pull it up cold and tell you their honest first impression
after thirty seconds. You'll learn more from that thirty seconds than from staring at it
yourself, because you can't see it with fresh eyes anymore.</p>

<h2>What This Adds Up To</h2>
<p>None of these five problems require a full rebuild to fix, and I want to be upfront about
that rather than using this as a scare tactic to sell a bigger project than you need. Sometimes
it's compressing a few images and adding a visible phone number. Sometimes the content is fine
and the whole thing just needs a faster host. The real value in going through this list isn't
finding out your site is terrible, most aren't. It's finding the one or two specific things that
are quietly costing you customers who never told you they left.</p>
<p>If you go through this checklist and find a few of these on your own site, that's normal, and
it's fixable. If you'd rather have a second set of eyes look it over and tell you honestly what's
worth fixing and what isn't, that's exactly the kind of audit I do before recommending any work
at all.</p>

<h2>Bottom Line</h2>
<p>A website doesn't have to be broken to underperform. Most of the time it's a handful of small,
fixable issues stacking up quietly in the background: a slow load here, a stale phone number
there, a missing call-to-action nobody thought to add. Individually minor. Together, they're the
difference between a site that works for your business and one that's just sitting there, online,
waiting for customers who already left.</p>
""",
    },
    {
        "slug": "how-to-write-a-cover-letter-that-actually-gets-read",
        "icon": "mail",
        "title": "How to Write a Cover Letter That Actually Gets Read in 2026",
        "description": "What actually makes a hiring manager read a cover letter instead of skipping it — the opening line, structure, and mistakes that get cover letters ignored.",
        "date": "August 15, 2026",
        "read_time": "6 min read",
        "excerpt": "Most cover letters get read for about six seconds before a hiring manager decides whether to keep going. Here's what actually earns the rest of their attention — and what gets a cover letter skipped entirely.",
        "body": """
<p>I write cover letters alongside resumes, and the question I get most isn't \"how do I write
one,\" it's \"does anyone even read these?\" Fair question. The honest answer is: sometimes, for
about six seconds, and then either they keep reading or they don't. What happens in those six
seconds is almost entirely in your control, and it has very little to do with the things most
cover letter advice obsesses over.</p>

<h2>Do You Actually Need One?</h2>
<p>If the application doesn't ask for a cover letter and doesn't give you anywhere to attach one,
don't manufacture a place to put it. But when there's an upload field for it, even one marked
\"optional,\" skipping it is a real cost. Optional fields are exactly where hiring managers look
for a signal of who actually wants the job versus who's mass-applying. A cover letter is one of
the few pieces of an application that can't be faked in bulk, which is precisely why it still
matters even in a process that's otherwise entirely automated.</p>

<h2>Why Most Cover Letters Get Skipped</h2>
<p>The letters that get skipped almost all make the same mistake in the first two sentences: they
restate the resume. \"I am writing to apply for the Marketing Coordinator position at Acme Co.
I have three years of experience in marketing and a degree in communications.\" A hiring manager
already has that information sitting right next to the letter. Repeating it in paragraph form
isn't a summary, it's dead weight, and it trains the reader to expect nothing new for the rest of
the page. Once that expectation sets in, most people stop reading closely, if they keep reading
at all.</p>

<h2>The Opening Line That Doesn't Get Ignored</h2>
<p>The first sentence has one job: give the reader a reason that isn't already sitting in your
resume. That usually means one of three things: a specific detail about the company that shows
you actually looked at it, a direct line to a real result you got somewhere else, or a genuine
reason this particular role is the one you want, not just a role. Compare \"I am excited to apply
for this position\" against \"Your job posting mentions rebuilding the onboarding flow, that's the
exact project I led at my last company, and it cut new-user drop-off by around a third.\" The
second one takes ten extra seconds to write and does more work than the entire rest of a generic
letter.</p>

<h2>The Structure That Actually Works</h2>
<p>Cover letters don't need to be clever, they need to be structured so a busy person can get the
point fast. A format that consistently works:</p>
<ul>
<li><strong>Opening line.</strong> The specific hook described above, not a restated job title.</li>
<li><strong>One paragraph, one story.</strong> Pick a single relevant result or project and tell it
like a short story with a real outcome, not a list of responsibilities. One good example beats
four vague ones.</li>
<li><strong>A direct line to their problem.</strong> Connect that story to something the job
posting actually mentions needing. This is the part most letters skip entirely, and it's the part
that makes a reader think \"this person read the posting,\" which is rarer than it should be.</li>
<li><strong>A short, confident close.</strong> Say plainly that you'd like to talk, not \"I look
forward to hearing from you,\" which says nothing. Thank them, and stop. Letters that trail off
apologizing for taking up someone's time undercut everything written above it.</li>
</ul>
<p>Three to four short paragraphs, done. If it's pushing past one page, it's saying too much.</p>

<h2>Mistakes That Quietly Kill a Cover Letter</h2>
<ul>
<li><strong>The wrong company name.</strong> Still happens constantly from letters written off a
template and never fully checked. It's an instant, unrecoverable red flag.</li>
<li><strong>Restating the resume word for word.</strong> Covered above, but worth repeating: this
is the single most common reason a letter stops getting read.</li>
<li><strong>Generic enthusiasm with nothing behind it.</strong> \"I've always been passionate about
this industry\" means nothing without a specific reason attached to it.</li>
<li><strong>Apologizing for gaps or a career change.</strong> If you're changing direction, say what
you're bringing with you, not why you're sorry for not following a straight line. Hiring managers
care far less about a nonlinear path than most applicants assume.</li>
<li><strong>Formatting fights with the resume.</strong> If you've cleaned up a resume to actually
get read by an <a href=\"/blog/how-to-beat-an-ats-resume-2026\">applicant tracking system</a>,
make sure the cover letter matches that same simple, readable structure. A polished resume paired
with a cluttered cover letter undercuts the work that went into the first one.</li>
</ul>

<h2>Bottom Line</h2>
<p>Nobody reads a cover letter front to back the way they'd read an email from a friend. They
skim the first two lines, decide whether the rest is worth their time, and either keep going or
move to the next application. Winning those two lines with something specific instead of generic
is what separates a cover letter that gets read from one that gets skipped, and it's a fixable
problem in about the time it takes to write four honest sentences.</p>
""",
    },
    {
        "slug": "how-to-write-a-linkedin-profile-that-actually-gets-you-noticed",
        "icon": "profile",
        "title": "How to Write a LinkedIn Profile That Actually Gets You Noticed in 2026",
        "description": "Why a LinkedIn profile isn't a resume copy-paste, the headline and About-section fixes that actually get you found in recruiter searches, and the mistakes that quietly bury a profile.",
        "date": "August 16, 2026",
        "read_time": "7 min read",
        "excerpt": "Recruiters don't read a LinkedIn profile the way they read a resume, they search it. Here's what actually gets a profile found, and the small fixes most people never make.",
        "body": """
<p>I rewrite LinkedIn profiles alongside resumes, and the two get treated the same way by most
people: write the resume, then paste the same bullet points into LinkedIn and call it done. That's
the single biggest miss. A resume gets read by one person after they've already decided to look at
it. A LinkedIn profile mostly gets found, through a recruiter search, a shared connection, someone
Googling your name before a call, and \"found\" only happens if the profile is built for search in
the first place.</p>

<h2>Recruiters Search LinkedIn, They Don't Read It</h2>
<p>Recruiter seats on LinkedIn come with a search tool that works a lot like a keyword filter: job
title, skills, location, years of experience. A recruiter searching \"project manager\" plus
\"healthcare\" plus \"Salesforce\" gets a results list, and your profile either has those literal
terms somewhere searchable or it doesn't show up at all, no matter how good your actual experience
is. This is the same logic as an applicant tracking system parsing a resume, just running on a
different platform. If your profile only says \"led cross-functional initiatives\" and never says
the actual job title or tools recruiters are typing into that search bar, you're invisible to a
search you'd otherwise be a strong match for.</p>

<h2>The Headline Isn't Your Job Title</h2>
<p>LinkedIn auto-fills your headline with your current job title, and most people just leave it
there. That's a wasted 220 characters. The headline shows up next to your name everywhere, search
results, comments, connection requests, so it's doing more work than almost any other field on the
profile. A stronger headline states what you do, who you do it for, and a real result or
specialty, not just a title. \"Marketing Coordinator at Acme Co.\" tells a reader nothing they
couldn't get from your current position. \"Marketing Coordinator | Email campaigns that grew a
subscriber list from 2K to 14K | B2B SaaS\" tells them what you're actually good at within about
two seconds.</p>

<h2>The About Section Nobody Reads Top to Bottom</h2>
<p>LinkedIn truncates the About section after roughly two to three lines before showing a \"see
more\" link, and most visitors never click it. That means whatever you put first is functionally
the whole section for a large share of readers. The version most people write starts with
something like \"Results-driven professional with 5+ years of experience...\", generic enough to
apply to almost anyone, and gives a reader zero reason to click further. Lead instead with the
same kind of specific hook that works in a cover letter: what you actually do, one real result, or
what kind of work you're looking for next. Save the fuller career story for the paragraphs after,
for the smaller number of people who do click through.</p>

<h2>Skills Section: What Actually Gets You Found</h2>
<p>The Skills section feeds directly into that recruiter search tool described above, so this is
not the place to list soft skills like \"team player\" or \"hard worker.\" Prioritize the specific
tools, platforms, certifications, and job-title language that someone would actually type into a
search bar looking for someone like you, the same literal-keyword-matching logic covered in
<a href=\"/blog/how-to-beat-an-ats-resume-2026\">how ATS software reads a resume</a>. Reorder the
list so your top three to five most relevant skills are pinned at the top; LinkedIn lets you
feature specific skills, and those are what show up most prominently.</p>

<h2>Mistakes That Quietly Bury a Profile</h2>
<ul>
<li><strong>No photo, or a bad one.</strong> Profiles with a photo get dramatically more views than
ones without, and a blurry selfie or old group photo undercuts the rest of the profile before
anyone reads a word.</li>
<li><strong>A headline that's just a job title.</strong> Covered above, but it's the single most
common miss on this platform.</li>
<li><strong>An About section left blank or barely filled in.</strong> An empty About section reads
as an unfinished profile, which reads as not serious about being found.</li>
<li><strong>Experience entries with no description.</strong> A job title and dates with nothing
underneath gives a reader, and the search algorithm, nothing to match against.</li>
<li><strong>Never updated after landing the last job.</strong> A profile that hasn't moved since
2022 signals someone who isn't actively engaged with their own career, even if that's not true.</li>
</ul>

<h2>Bottom Line</h2>
<p>A resume gets read once someone's already decided to look at it. A LinkedIn profile has to earn
that decision first, through search, through a quick scan, through whatever shows before someone
clicks \"see more.\" Building it around how it actually gets found, real keywords, a headline that
says something, an About section that leads with the good part, matters more than how polished the
full career story reads underneath it.</p>
""",
    },
    {
        "slug": "behind-the-scenes-on-a-real-client-project-part-1",
        "icon": "progress",
        "title": "Behind the Scenes on a Real Client Project: Part 1",
        "description": "An honest look at a live copywriting and web content project, what's working, what hasn't gone smoothly, and what I'm waiting on right now. Part 1 of 2.",
        "date": "August 17, 2026",
        "read_time": "6 min read",
        "excerpt": "Most of what people see from a freelancer is the finished result. Here's what an actual project looks like while it's still in progress, the strengths, the friction, and what I'm waiting on right now.",
        "body": """
<p>Most of what a potential client sees from me is a finished portfolio piece, a clean before-and-
after, a case study with a bow on it. That's useful, but it skips the part where the actual work
happens. I'm in the middle of a real project right now, a homepage and product copy rewrite for a
small lifestyle brand, and I wanted to write about it while it's still unfinished instead of
waiting until it's polished. I'm keeping the client and the business itself anonymous here, this
isn't about them, it's about what the process actually looks like from the inside. This is part
one. I'll write a follow-up once the project wraps.</p>

<h2>What the Project Actually Is</h2>
<p>The scope: rewrite the homepage copy, rewrite four product descriptions, pull together a real
founder story for the About section, and audit the site's existing images for anything that reads
as generic or AI-generated, with real replacement recommendations. No redesign, no new layout,
just the words and the photography, built to sound like an actual person instead of templated
marketing copy. It's broken into two milestones: a first draft for review, then a final round
after feedback.</p>

<h2>Why I Almost Sent the Wrong First Draft</h2>
<p>Early on, I wrote a full placeholder version of the homepage copy, hero section, mission
statement, FAQ, written the way I imagined the founder might sound. It was fine. It was also
generic in exactly the way I write about avoiding on this blog, competent copy that could have
belonged to a dozen similar brands. I made the call not to send it. Instead I sent over a short
list of real questions: the actual founder story, what he was proudest of in the products, what he
wanted the site to feel like. That one decision, holding the placeholder instead of shipping it,
is probably the single biggest reason the final draft ended up sounding like an actual person
rather than a guess at one.</p>
<p>When the real story came back, it was more specific and more honest than anything I could have
invented, real family history, a real turning point, real reasons behind why the business exists
at all. That's the material that actually makes copy land. Guessing at a founder's voice instead
of asking for it is a shortcut that shows.</p>

<h2>The Image Audit Turned Up More Than Expected</h2>
<p>I went through the site's existing photography image by image, and it turned out to have more
problems than a quick glance would suggest: a stock photo in the mission section with zero actual
connection to what the brand does (the client's own top complaint once I flagged it), a couple of
product photos with the telltale signs of AI generation, an oddly warped hand, lighting that was
too evenly \"perfect\" to be a real photograph, and the same lifestyle photos reused across
multiple product listings, a small thing that quietly signals a templated site to anyone paying
attention. I sourced real, properly licensed replacement photos for each flagged spot rather than
just listing the problems and leaving it there.</p>

<h2>What's Gone Well</h2>
<ul>
<li><strong>The real founder material elevated everything.</strong> Once I had the actual story
instead of a guess, the homepage and About section stopped needing much revision at all.</li>
<li><strong>The client caught things I might have missed.</strong> He immediately agreed the
mission-section photo was wrong the moment I flagged it, he'd apparently felt that way for a while
without knowing how to fix it.</li>
<li><strong>Milestone one landed clean.</strong> The first full deliverable, a complete draft PDF
with the homepage copy, product descriptions, founder story, and image audit, was approved and
paid without requested revisions.</li>
</ul>

<h2>What Hasn't Gone Smoothly</h2>
<ul>
<li><strong>Silence after approval isn't the same as feedback.</strong> The client approved the
milestone and activated the next one, but didn't leave written notes on what he actually thought
of the draft. Approval tells me he didn't hate it. It doesn't tell me what to adjust before the
final round, so I had to follow up directly and ask.</li>
<li><strong>Placeholder copy is a real time cost, even when you catch it.</strong> Writing the
first full homepage draft before deciding not to use it wasn't wasted exactly, it clarified what
I actually needed to ask, but it's a step I'd try to skip earlier next time by asking the founder
questions before writing anything client-facing.</li>
</ul>

<h2>What I'm Waiting On Right Now</h2>
<p>Specific feedback on the first draft before I move into the final polish pass. The project isn't
stalled, the milestone structure means work can continue either way, but I'd rather adjust based
on what he actually thinks than guess at revisions he didn't ask for. That's the honest state of
things as of this post.</p>

<h2>Why I'm Writing This At All</h2>
<p>Anyone can post a finished result. Fewer people show the part where a decision could have gone
wrong, the placeholder draft I didn't send, or the part where a client goes quiet and you just
have to follow up like a normal person. That's what the work actually looks like most of the time,
and I'd rather be honest about that than only show the polished after photo. Part two goes up once
this one's finished, revisions and all.</p>
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
