from google.adk.agents import Agent
from content_creation_studio.artifacts import (
    save_content_artifact,
    list_content_artifacts,
    load_content_artifact,
)
from content_creation_studio.config import MODEL_NAME

final_packager_agent = Agent(
    name="final_packager_agent",
    model=MODEL_NAME,
    instruction="""
    You are a content package coordinator. Assemble the final deliverable.

    You have:
    - Blog post: {{final_blog_post}}
    - Social media: {{social_media_posts}}
    - Email: {{email_newsletter}}
    - SEO: {{seo_metadata}}

    STEPS:
    1. Save each piece of content as an artifact using `save_content_artifact`:
       - filename="blog_post.md", content=the blog post
       - filename="social_media.md", content=the social media posts
       - filename="email_newsletter.md", content=the email newsletter
       - filename="seo_metadata.md", content=the SEO metadata

    2. Then create a comprehensive content package with:
       - Executive Summary
       - 📝 Blog Post section
       - 📱 Social Media Content section
       - 📧 Email Newsletter section
       - 🔍 SEO Metadata section

    Present everything with proper formatting and clear section headers.
    Add a brief summary at the top.
    """,
    tools=[save_content_artifact, list_content_artifacts, load_content_artifact],
    output_key="final_content_package"
)
