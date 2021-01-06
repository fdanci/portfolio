from portfolio_app.models import PortfolioUrls


def portfolio_urls_renderer(_):
    """
    Read urls from database and return them.

    :return: The urls as template context.
    """
    portfolio_urls = PortfolioUrls.objects.all()[0]

    resume_url = portfolio_urls.resume_url
    linkedin_url = portfolio_urls.linkedin_url
    github_url = portfolio_urls.github_url

    return {
        'resume_url': resume_url,
        'linkedin_url': linkedin_url,
        'github_url': github_url,
    }
