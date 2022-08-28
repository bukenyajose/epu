import xml.etree.cElementTree as ET

from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect

from main.models import Blog, Candidate, Member

# Create your views here.
def home_view(request):
    news = Blog.objects.all()
    members = Member.objects.exclude(is_external=True)
    candidates = Candidate.objects.all()

    context = {
        "news": news,
        "members": members,
        "candidates": candidates,
        "title": "Home",
        "description": "The Uganda Greens Party",
        "keywords": ""
    }
    return render(request, 'main/index.html', context)

def about_view(request):
    team = Member.objects.all()
    context = {
        "team": team,
        "active": 'about',
        "title": "About",
        "description": "The Uganda Greens Party",
        "keywords": ""
    }
    return render(request, 'main/about.html', context)

def contact_view(request):
    if request.method == "POST":
        name: str = request.POST["name"]
        email: str = request.POST["email"]
        subject: str = request.POST["subject"]
        message: str = request.POST["message"]

        # body = subject + message
        # reqUrl = "https://spam.drexsoft.org/"

        # headersList = {
        #     "Accept": "*/*",
        #     "User-Agent": "Keyra Safaris (https://www.keyrasafaris.com)",
        #     "Content-Type": "application/json",
        # }

        # payload = json.dumps({"query": body})

        # response = requests.request("POST", reqUrl, data=payload, headers=headersList)
        # spam = json.loads(response.text)["label"]

        # if (
        #     spam == "spam"
        #     or "Vaw" in name
        #     or name == "HenryVaw"
        #     or name == "Henry Vaw"
        #     or name == "CrytoVawVaw"
        #     or name.lower() == "henryvaw"
        #     or name.lower() == "crytovawvaw"
        #     or name.lower() == "cryto vawvaw"
        #     or name.lower() == "crytovaw vaw"
        #     or name.lower() == "cryto vaw vaw"
        #     or message.endswith("https://Vaw.187sued.de/gotodate/promo ")
        # ):
        #     pass
        # else:
        send_mail(
            subject=subject,
            message=f"{name}({email})\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_TO_EMAIL],
        )
        messages.success(
            request,
            "Thanks For contacting us, your message has been sent Successfully!",
        )
    context = {
        "active": 'contact',
        "title": "Contact",
        "description": "Best Travels Company",
        "keywords": "travel, tour, safari, agency"
    }
    return render(request, 'main/contact.html', context)

def news_view(request):
    posts = Blog.objects.all()
    context = {
        "posts": posts,
        "active": 'news',
        "title": "News",
        "description": "Uganda Greens Party",
        "keywords": ""
    }
    return render(request, 'main/blog-grid.html', context)

def blog_details_view(request, year, month, day, slug, id):
    post = get_object_or_404(Blog, id=id, slug=slug)
    context = {
        "post": post,
        "title": post.title,
        "description": "The Uganda Greens Party",
        "keywords": ""
    }
    return render(request, 'main/blog-details.html', context)

def generate_sitemap(request):

    _url = "https://www.ecologicalpartyofuganda.com"
    dt = datetime.now().strftime("%Y-%m-%d")

    schema_loc = ("http://www.sitemaps.org/schemas/sitemap/0.9 "
                  "http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd")

    root = ET.Element("urlset")
    root.attrib['xmlns:xsi'] = 'http://www.w3.org/2001/XMLSchema-instance'
    root.attrib['xsi:schemaLocation'] = schema_loc
    root.attrib['xmlns'] = "http://www.sitemaps.org/schemas/sitemap/0.9"

    doc = ET.SubElement(root, "url")
    ET.SubElement(doc, "loc").text = _url
    ET.SubElement(doc, "lastmod").text = dt
    ET.SubElement(doc, "changefreq").text = 'weekly'
    ET.SubElement(doc, "priority").text = "1.0"

    doc = ET.SubElement(root, "url")
    ET.SubElement(doc, "loc").text = f"{_url}/#about"
    ET.SubElement(doc, "lastmod").text = dt
    ET.SubElement(doc, "changefreq").text = 'weekly'
    ET.SubElement(doc, "priority").text = "1.0"

    doc = ET.SubElement(root, "url")
    ET.SubElement(doc, "loc").text = f"{_url}/#principles"
    ET.SubElement(doc, "lastmod").text = dt
    ET.SubElement(doc, "changefreq").text = 'weekly'
    ET.SubElement(doc, "priority").text = "1.0"

    doc = ET.SubElement(root, "url")
    ET.SubElement(doc, "loc").text = f"{_url}/#candidates"
    ET.SubElement(doc, "lastmod").text = dt
    ET.SubElement(doc, "changefreq").text = 'weekly'
    ET.SubElement(doc, "priority").text = "1.0"

    doc = ET.SubElement(root, "url")
    ET.SubElement(doc, "loc").text = f"{_url}/#members"
    ET.SubElement(doc, "lastmod").text = dt
    ET.SubElement(doc, "changefreq").text = 'weekly'
    ET.SubElement(doc, "priority").text = "1.0"

    doc = ET.SubElement(root, "url")
    ET.SubElement(doc, "loc").text = f"{_url}/#news"
    ET.SubElement(doc, "lastmod").text = dt
    ET.SubElement(doc, "changefreq").text = 'weekly'
    ET.SubElement(doc, "priority").text = "1.0"

    doc = ET.SubElement(root, "url")
    ET.SubElement(doc, "loc").text = f"{_url}/#contact"
    ET.SubElement(doc, "lastmod").text = dt
    ET.SubElement(doc, "changefreq").text = 'weekly'
    ET.SubElement(doc, "priority").text = "1.0"

    blogs = Blog.objects.all()


    for post in blogs:
        doc = ET.SubElement(root, "url")
        ET.SubElement(doc, "loc").text = f"{_url}{post.get_absolute_url()}"
        ET.SubElement(doc, "lastmod").text = dt
        ET.SubElement(doc, "changefreq").text = 'weekly'
        ET.SubElement(doc, "priority").text = "0.9"

    tree = ET.ElementTree(root)
    tree.write("templates/sitemap.xml",
               encoding='utf-8', xml_declaration=True)

    return redirect("/sitemap.xml")
