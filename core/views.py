from django.shortcuts import render
from .models import Session, Answer
from collections import defaultdict

QUESTIONS_S = [
    "Что происходит сейчас?",
    "Когда это возникает?",
    "Как ты понимаешь, что это проблема?",
]


def step_s(request):
    if request.method == "GET":
        session = Session.objects.create()
        request.session["session_id"] = session.id
        print("SESSION CREATED:", session.id)
        step = 0

    else:
        session_id = request.session.get("session_id")
        session = Session.objects.get(id=session_id)

        step = int(request.POST.get("step", 0))
        answer = request.POST.get("answer")

        Answer.objects.create(
            session=session,
            step="S",
            question=QUESTIONS_S[step],
            answer=answer,
            order=step
        )

        print("S SAVED")

        step += 1

    if step >= len(QUESTIONS_S):
        return render(request, "core/done.html")

    return render(request, "core/step.html", {
        "question": QUESTIONS_S[step],
        "step": step
    })

def step_c(request):
    MAX_DEPTH = 5

    # получаем сессию
    session_id = request.session.get("session_id")
    if not session_id:
        return render(request, "core/error.html")

    session = Session.objects.get(id=session_id)
    answers = Answer.objects.filter(session=session, step="C").order_by("order")

    if request.method == "POST":
        depth = int(request.POST.get("depth", 0))
        answer = request.POST.get("answer")

        # 🔥 СОХРАНЕНИЕ
        Answer.objects.create(
            session=session,
            step="C",
            question="Почему?" if depth > 0 else "Причина",
            answer=answer,
            order=depth
        )

        print(f"C уровень {depth}: {answer}")
        print("C SAVED")

        depth += 1
    else:
        depth = 0

    if depth >= MAX_DEPTH:
        return render(request, "core/done_c.html")

    if depth == 0:
        question = "В чем причина этой ситуации?"
    else:
        prev_answer = answers.last().answer if answers.exists() else ""

        question = f"Почему: \"{prev_answer}\"?"

    return render(request, "core/step_c.html", {
        "question": question,
        "depth": depth
    })

def step_o(request):
    QUESTIONS_O = [
        "Чего ты хочешь вместо этого?",
        "Как ты поймешь, что достиг результата?",
        "Где и когда это должно происходить?",
        "Зависит ли это от тебя?"
    ]

    # 🔥 получаем сессию
    session_id = request.session.get("session_id")
    if not session_id:
        return render(request, "core/error.html")

    session = Session.objects.get(id=session_id)

    if request.method == "POST":
        step = int(request.POST.get("step", 0))
        answer = request.POST.get("answer")

        # 🔥 СОХРАНЕНИЕ
        Answer.objects.create(
            session=session,
            step="O",
            question=QUESTIONS_O[step],
            answer=answer,
            order=step
        )

        print(f"O {step}: {answer}")
        print("O SAVED")

        step += 1
    else:
        step = 0

    if step >= len(QUESTIONS_O):
        return render(request, "core/done_o.html")

    return render(request, "core/step_o.html", {
        "question": QUESTIONS_O[step],
        "step": step
    })

def step_r(request):
    QUESTIONS_R = [
        "Какие ресурсы у тебя уже есть?",
        "Когда у тебя уже получалось что-то похожее?",
        "Кто или что может тебе помочь?",
        "В каком состоянии тебе нужно быть?"
    ]

    # 🔥 получаем сессию
    session_id = request.session.get("session_id")
    if not session_id:
        return render(request, "core/error.html")

    session = Session.objects.get(id=session_id)

    if request.method == "POST":
        step = int(request.POST.get("step", 0))
        answer = request.POST.get("answer")

        # 🔥 СОХРАНЕНИЕ
        Answer.objects.create(
            session=session,
            step="R",
            question=QUESTIONS_R[step],
            answer=answer,
            order=step
        )

        print(f"R {step}: {answer}")
        print("R SAVED")

        step += 1
    else:
        step = 0

    if step >= len(QUESTIONS_R):
        return render(request, "core/done_r.html")

    return render(request, "core/step_r.html", {
        "question": QUESTIONS_R[step],
        "step": step
    })

def step_e(request):
    QUESTIONS_E = [
        "Что изменится, когда ты достигнешь этого?",
        "Как это повлияет на твою жизнь?",
        "Есть ли какие-то негативные последствия?",
        "Тебе точно это подходит?"
    ]

    # 🔥 получаем сессию
    session_id = request.session.get("session_id")
    if not session_id:
        return render(request, "core/error.html")

    session = Session.objects.get(id=session_id)

    if request.method == "POST":
        step = int(request.POST.get("step", 0))
        answer = request.POST.get("answer")

        # 🔥 СОХРАНЕНИЕ
        Answer.objects.create(
            session=session,
            step="E",
            question=QUESTIONS_E[step],
            answer=answer,
            order=step
        )

        print(f"E {step}: {answer}")
        print("E SAVED")

        step += 1
    else:
        step = 0

    if step >= len(QUESTIONS_E):
        return render(request, "core/done_all.html", {
            "session_id": session.id
        })

    return render(request, "core/step_e.html", {
        "question": QUESTIONS_E[step],
        "step": step
    })

def report(request, session_id):
    session = Session.objects.get(id=session_id)
    answers = Answer.objects.filter(session=session).order_by("step", "order")

    data = defaultdict(list)

    for ans in answers:
        data[ans.step].append(ans)

    return render(request, "core/report.html", {
        "data": data,
        "session": session
    })