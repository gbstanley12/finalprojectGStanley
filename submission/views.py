from django.shortcuts import render
from .forms import TextSubmissionForm
from .models import TextSubmission
import textstat


def submit_text(request):
    if request.method == 'POST':
        form = TextSubmissionForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            submission_text = form.cleaned_data['submission_text']
            word_count = len(submission_text.split())

            # Create TextSubmission instance
            submission = TextSubmission(title=title, submission_text=submission_text, word_count=word_count)

            # Calculate readability scores
            submission.flesch_reading_ease = textstat.flesch_reading_ease(submission_text)
            # ... calculate other scores

            submission.save()

            # Redirect or show success message
            # ...

    else:
        form = TextSubmissionForm()

    return render(request, 'submission/submit_text.html', {'form': form})
