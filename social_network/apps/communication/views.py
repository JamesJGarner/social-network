from .models import Message, Reply


class MessagesList(ListView):
    model = Message

    def get_queryset(self):
        qs = super(MessagesList, self).get_queryset()
        qs = qs.filter(to_user=self.request.user.id)
        return qs



class MessagesSent(ListView):
    model = Message
    template_name_suffix = '_sent'
    def get_queryset(self):
        qs = super(MessagesSent, self).get_queryset()
        qs = qs.filter(from_user=self.request.user.id)
        return qs


class MessageForm(CreateView):
    model = Message

    form_class = MessageForm
    success_url = '/'
    def form_valid(self, form):
        MessageForm = form.save(commit=False)
        MessageForm.from_user = self.request.user
        MessageForm.date = datetime.now()
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)

class Reply(CreateView):
    model = Reply
    form_class = ReplyForm
    success_url = '/'
    def form_valid(self, form):
        MessageForm = form.save(commit=False)
        MessageForm.user = self.request.user
        MessageForm.date = datetime.now()
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)

class MessageDetail(DetailView):
    model = Message
    def get_object(self, queryset=None):
        obj = super(MessageDetail, self).get_object()
        if self.request.user == obj.to_user:
            obj.read = True
            obj.save()


        if not self.request.user.id in (obj.to_user.id , obj.from_user.id):
            raise Http404
        return obj


    def form_valid(self, form):
        MessageForm = form.save(commit=False)
        MessageForm.from_user = self.request.user
        MessageForm.date = datetime.now()
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)

