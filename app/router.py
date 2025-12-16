from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "What is the return policy?",
        "What is your replacement policy?",
        "How do you handle defective or damaged items?",
        "What is your policy on faulty products?",
        "Can I get a refund for a defective product?",
        "How long does a refund take?",
        "What is the customer service policy?",
        "What is the warranty policy?"
    ],
    score_threshold=0.30
)   

sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% /discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ],
    score_threshold=0.30
)

small_talk = Route(
    name='small-talk',
    utterances=[
        "How are you?",
        "What is your name?",
        "Are you a robot?",
        "What are you?",
        "What do you do?",
    ],
    score_threshold=0.30
)   
routes = [faq, sql, small_talk]

router = SemanticRouter(encoder=encoder, routes=routes, auto_sync="local")

if __name__ == "__main__":
    print(router("What is your policy on defective product?"))
    print(router("What is refund policy?"))
    print(router("Do you take cash as a payment option?"))
    print(router("Pink Puma shoes in price range 5000 to 1000"))