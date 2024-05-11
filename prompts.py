prompts = {
    "en": {
        "summarize": "Please summarize the text beetween ==START TEXT== and ==END TEXT== in one or two sentences, do no add comments:\n\n==START TEXT==\n\n{payload}\n\n==END TEXT==\n",
        "translate": "Please translate the text beetween ==START TEXT== and ==END TEXT== to French, do no add comments:\n\n==START TEXT==\n\n{payload}\n\n==END TEXT==\n",
        "extend": "Please extend the bullet list beetween ==START TEXT== and ==END TEXT== in a few paragraphs, do no add comments:\n\n==START TEXT==\n\n{payload}\n\n==END TEXT==\n",
    },
    "fr": {
        "summarize": "Veuillez résumer le texte entre ==DEBUT TEXTE== et ==FIN TEXTE== en une ou deux phrases, sans ajouter de commentaires :\n\n==DEBUT TEXTE==\n\n{payload}\n\n==FIN TEXTE==\n",
        "translate": "Veuillez traduire le texte entre ==DEBUT TEXTE== et ==FIN TEXTE== en Anglais, ne pas ajouter de commentaires :\n\n==DEBUT TEXTE==\n\n{payload}\n\n==FIN TEXTE==\n",
        "extend": "Veuillez détailler la liste entre ==DEBUT TEXTE== et ==FIN TEXTE== sous forme de quelques paragraphes :\n\n==DEBUT TEXTE==\n\n{payload}\n\n==FIN TEXTE==\n",
    },
}