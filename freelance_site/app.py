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
