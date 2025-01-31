from bs4 import BeautifulSoup
import requests

def fetch_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # check for request success
        soup = BeautifulSoup(response.text, 'html.parser') # store parsed html
        
        # find article or main tag on html
        main_content = soup.find('article') or soup.find('main')
        if main_content:
            # get text from article/main html tags
            # join adjacent text nodes
            # remove whitespace
            text = main_content.get_text(separator=" ", strip=True)
            # debug
            print("Found Article/Main \n")
            return clean_content(text)

        # fallback: Extract all paragraphs if <article> or <main> is not found
        paragraphs = soup.find_all('p')
        if paragraphs:
            text = " ".join([p.get_text(separator=" ", strip=True) for p in paragraphs])
            # debug
            print("Found Paragraphs\n")
            return clean_content(text)
        
        # If no meaningful content found, return the entire page text
        return clean_content(soup.get_text(separator=" ", strip=True))

        # debug
        print("Found Nothing\n")

    except requests.exceptions.RequestException as e:
        return f"Error fetching webpage: {e}"

def clean_content(text):
    # Removes boilerplate text like disclaimers, navigation menus, and footers.
    irrelevant_phrases = [
        # Navigation
        "Home", "About Us", "Contact Us", "Privacy Policy", "Terms of Service",
        "Help Center", "FAQ", "Support", "Login", "Sign In", "Register",
        "Dashboard", "My Account", "Settings", "Logout", "Careers", "Blog",
        "Press", "Investor Relations", "Accessibility", "Advertise with Us", "Open acess"

        # Disclaimers & Legal Notices
        "All rights reserved.", "This site uses cookies to improve your experience.",
        "By using this site, you agree to our Terms and Conditions.",
        "This website is for informational purposes only.",
        "No legal, financial, or medical advice is provided.", "Use at your own risk.",
        "This site contains affiliate links.", "Trademarks belong to their respective owners.",

        # Security & Privacy Notices
        "We value your privacy.", "We do not sell or share your personal data.",
        "Your data is protected under GDPR/CCPA.",
        "This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.",

        # Call-to-Action (CTA) Phrases
        "Click here to learn more.", "Subscribe to our newsletter.", "Follow us on social media.",
        "Read more.", "Get started today.", "Join now for free.",

        # Footer Content
        "©", "Follow us on", "Powered by", "Made with ❤️ by", "Sitemap"
    ]
    
    for phrase in irrelevant_phrases:
        text = text.replace(phrase, "")
    
    return text.strip()


if __name__ == "__main__":
    test_url = "https://nida.nih.gov/research-topics/addiction-science/drugs-brain-behavior-science-of-addiction"
    content = fetch_web_content(test_url)
    print(content)


'''
things to look for:

<section id="abstract">

test links:
https://arxiv.org/html/2501.13833v1
https://pmc.ncbi.nlm.nih.gov/articles/PMC3860451/
https://nida.nih.gov/research-topics/addiction-science/drugs-brain-behavior-science-of-addiction
"https://dl.acm.org/doi/10.1145/3527155"

'''
