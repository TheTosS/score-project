from django.shortcuts import render

QUESTIONS_S = [
    "Что происходит сейчас?",
    "Когда это возникает?",
    "Как ты понимаешь, что это проблема?",
]


def step_s(request):
    if request.method == "POST":
        step = int(request.POST.get("step", 0))
        answer = request.POST.get("answer")
        print(f"Ответ {step}: {answer}")
        step += 1
    else:
        step = 0  # первый заход

    if step >= len(QUESTIONS_S):
        return render(request, "core/done.html")

    return render(request, "core/step.html", {
        "question": QUESTIONS_S[step],
        "step": step
    })

def step_c(request):
        MAX_DEPTH = 5

        if request.method == "POST":
            depth = int(request.POST.get("depth", 0))
            answer = request.POST.get("answer")

            print(f"C уровень {depth}: {answer}")

            depth += 1
        else:
            depth = 0

        if depth >= MAX_DEPTH:
            return render(request, "core/done_c.html")

        if depth == 0:
            question = "В чем причина этой ситуации?"
        else:
            question = f"Почему это? ({depth + 1}/5)"

        return render(request, "core/step_c.html", {
            "question": question,
            "depth": depth


    })