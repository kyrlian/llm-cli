prompts = {
    "en": {
        "summarize": "Please summarize the following TEXT in one or two sentences, do no add comments:\n\nTEXT\n\n{payload}\n",
        "translate": "Please translate the following TEXT to French, do no add comments:\n\nTEXT\n\n{payload}\n",
        "extend": "Please extend the following BULLET LIST in a few paragraphs, do no add comments:\n\BULLET LIST\n\n{payload}\n",
    },
    "fr": {
        "summarize": "Veuillez résumer le TEXTE suivant en une ou deux phrases, sans ajouter de commentaires :\n\nTEXTE\n\n{payload}\n",
        "translate": "Veuillez traduire le texte suivant en Anglais, ne pas ajouter de commentaires :\n\nTEXT\n\n{payload}\n",
        "extend": "Veuillez détailler la LISTE suivante sous forme de quelques paragraphes :\n\nLISTE\n\n{payload}\n",
    },
}