import json, os

import openai
import pdb


class Chatter:
    def __init__(self):

        openai.api_key = os.getenv("OPENAI_API_KEY")

        return None

    def get_response(self, prompt, job):
        """Basic ChatGPT query. Give a prompt, get a response.

        Parameters
        ----------
        prompt : str
            the instructions/dialogue provided to ChatGPT
        """
        # print(prompt)
        # pdb.set_trace()
        response_list = []
        for i in range(int(job["template_results"])):
            message = openai.Completion.create(
              model="text-davinci-003",
              prompt=prompt,
              temperature=0.7,
              max_tokens=int(job["tokens"]),
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
            response_list.append(message.choices[0].text)
        return response_list
        # return message.choices[0].text

    def parse_job(self, job):
        """Creates a prompt from a job dict

        Parameters
        ----------
        job : dict
            expects a job dict as defined in app.py
            {
                "subject": subject,
                "tokens": tokens,
                "sender_ages": sender_ages,
                "recipient_ages": recipient_ages,
                "trends": trends,
                "no_variable": no_variable,
                "languages": languages,
                "template_results": template_results
            }
        """

        # if job["template_results"] != "a":
        #     prompt = "Write %s examples " % job["template_results"]
        # else:
        prompt = "Write an example email "
        # if job["template_results"] in ["2", "3"]:
        #     prompt += "emails "
        # else:
        #     prompt += "email "
        if job["tokens"] != "":
            prompt += "with no more than %s characters " % job["tokens"]
        if job["languages"] == "日本語":
            prompt += " %s." % "japanese"
        elif job["languages"] == "english":
            prompt += " %s." % "english"
        else:
            prompt += " %s." % job["languages"]
        if job["sender_ages"] == "30代女性":
            prompt += "from %s " % "a female in her 30s "
        elif job["sender_ages"] == "40代女性":
            prompt += "from %s " % "a female in her 40s "
        else:
            prompt += "from %s " % "a female in her 50s "
        if job["recipient_ages"] == "30代女性":
            prompt += "to a target who is %s " % "a female in her 30s."
        elif job["recipient_ages"] == "40代女性":
            prompt += "to a target who is %s " % "a female in her 40s."
        else:
            prompt += "to a target who is %s " % "a female in her 50s."
        if job["subject"] != "":
            prompt += "The email must has the subject line '%s' " % job["subject"]
        if job["no_variable"] != "":
            prompt += "and its content theme is about '%s' ." % job["no_variable"]

        while prompt[-1] == " ":
            prompt = prompt[:-1]
        return prompt

    def email_from_job(self, job):
        """Given a job dict, generates an email.

        Parameters
        ----------
        job : dict
            expects a job dict as defined in app.py
            {
                "subject": subject,
                "tokens": tokens,
                "sender_ages": sender_ages,
                "recipient_ages": recipient_ages,
                "trends": trends,
                "no_variable": no_variable,
                "languages": languages,
                "template_results": template_results
            }
        """
        prompt = self.parse_job(job)
        messages = self.get_response(prompt, job)
        return messages
