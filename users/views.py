from django.http import JsonResponse
import json
from users.models import Question
from django.utils import timezone
from question_choice_log import get_logger

lg = get_logger(name="(question_log)", file_name="question_choice.log")


def create_question(request):
    """create a question using Post man

    Args:
        request: sending request from post man

    Returns:
        response in the form of json format
    """
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            lg.info(data)
            q = Question(question_text=data.get("question_text"),
                         published_date=timezone.now())
            q.save()
            lg.debug(q)
            lg.debug("question saved successfully")
            return JsonResponse({"message": f"{q} question saved successfully"})
    except Exception as e:
        lg.error(e)


def retrieve_question(request):
    """retrieve a question using Post man

    Args:
        request: sending request from post man

    Returns:
        response in the form of json format
    """
    try:
        if request.method == "GET":
            question = Question.objects.all()
            data = {
                "question": list(question.values())
            }
            lg.debug(data)
            lg.debug("retrieved all question successfully")
            return JsonResponse(data)
    except Exception as e:
        lg.error(e)


def update_question(request):
    """update a question using Post man

    Args:
        request: sending request from post man

    Returns:
        response in the form of json format
    """
    try:
        if request.method == "PUT":
            data = json.loads(request.body)
            lg.info(data)
            question = Question.objects.get(id=data.get("question_id"))
            if not question:
                return JsonResponse({"message": "data not found"})
            question.question_text = data.get("question_text")
            question.save()
            lg.debug(question)
            lg.debug("question successfully updated")
            return JsonResponse({"message": "question successfully updated"})
    except Exception as e:
        print(e)


def delete_question(request):
    """delete a question using Post man

    Args:
        request: sending request from post man

    Returns:
        response in the form of json format
    """
    try:
        if request.method == "DELETE":
            data = json.loads(request.body)
            question = Question.objects.get(id=data.get("question_id"))
            if not question:
                return JsonResponse({"message": "data not found"})
            lg.info(question)
            question.delete()
            question.save()
            lg.debug(question)
            lg.debug("question successfully deleted")
            return JsonResponse({"message": "question successfully deleted"})
    except Exception as e:
        lg.info(e)


def create_choice(request):
    """create a choice with question_id, choice_text and votes using Post man

    Args:
        request: sending request from post man

    Returns:
        response in the form of json format
    """
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            q = Question.objects.get(pk=data.get("question_id"))
            q.choice_set.create(choice_text=data.get(
                "choice_text"), votes=data.get("votes"))
            q.save()
            print(q.choice_set.all())
            print(q.choice_set.count())
            lg.debug("choice successfully saved")
            return JsonResponse({"message": "choice saved succesfully"})
    except Exception as e:
        lg.error(e)


def retrieve_choice(request):
    """retrieve a choice using Post man

    Args:
        request: sending request from post man

    Returns:
        response in the form of json format
    """
    try:
        if request.method == "GET":
            data = json.loads(request.body)
            q = Question.objects.get(pk=data.get("question_id"))
            choices = q.choice_set.all()
            data = {
                "choices": list(choices.values())
            }
            lg.debug(data)
            lg.debug(" retreived choice successfully")
            return JsonResponse(data)
    except Exception as e:
        lg.error(e)


def update_choice(request):
    """update a choice using Post man

    Args:
        request: sending request from post man

    Returns:
        response in the form of json format
    """
    try:
        if request.method == "PUT":
            data = json.loads(request.body)
            choice = Question.objects.get(pk=data.get("question_id"))
            if not choice:
                return JsonResponse({"message": "data not found"})
            choice.choice_text = data.get("choice_text")
            choice.save()
            lg.debug("choice successfully updated")
            return JsonResponse({"message": "choice successfully updated"})
    except Exception as e:
        lg.error(e)


def delete_choice(request):
    """create a choice using Post man

    Args:
        request: sending request from post man

    Returns:
        response in the form of json format
    """
    try:
        if request.method == "DELETE":
            data = json.loads(request.body)
            choice = Question.objects.get(pk=data.get("question_id"))
            if not choice:
                return JsonResponse({"message": "data not found"})
            choice.delete()
            choice.save()
            lg.debug("choice successfully deleted")
            return JsonResponse({"message": "choice successfully deleted"})
    except Exception as e:
        lg.error(e)
