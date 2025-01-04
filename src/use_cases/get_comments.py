from gateways.linkedin_gateway import LinkedInGateway

class GetCommentsUseCase:
    def __init__(self, linkedin_gateway: LinkedInGateway):
        self.linkedin_gateway = linkedin_gateway

    def execute(self, url):
        comments = self.linkedin_gateway.fetch_comments(url)
        return [comment.to_dict() for comment in comments]