import json
from use_cases.get_comments import GetCommentsUseCase
from gateways.linkedin_gateway import LinkedInGateway


def lambda_handler(event, context):

    body = json.loads(event["body"])
    url = body["url"]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.linkedin.com/",
        "Cookie": 'JSESSIONID=ajax:8532057280926944007; lang=v=2&lang=pt-br; bcookie="v=2&af40bf4f-4298-4846-8167-4a3daa697c51"; bscookie="v=1&20250103030059f38a0a60-0cde-401c-85ab-9ec37204b93aAQHnLMtJ5HApYiFLC4LTyBe6n70igDD6"; lidc="b=OGST05:s=O:r=O:a=O:p=O:g=3261:u=1:x=1:i=1735972074:t=1736058474:v=2:sig=AQGW87v-UaVV0UX32lsecftCkYL7ex9N"; __cf_bm=bGXdNs3jV9L6uUEqB_hWS25AmNUWIW4CPExM8JrILNE-1735972075-1.0.1.1-hqdlsvxSXe15iG_7o97g_.Hz7QkNFNg9wBNaw8Rsav7e4E5_PmwECU87sZ4InhP.qsBQSkbWWzKLQ2CvA58myg'
    }

    linkedin_gateway = LinkedInGateway(headers)
    get_comments_use_case = GetCommentsUseCase(linkedin_gateway)

    # Executando o caso de uso
    comments = get_comments_use_case.execute(url)

    # Retornando a resposta
    return {
        "statusCode": 200,
        "body": json.dumps(comments),
    }