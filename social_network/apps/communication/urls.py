from .views import MessagesList, MessageForm, MessageDetail, MessagesSent, MessageReply


    url(r'^messages/(?P<pk>\d+)/$', MessageDetail.as_view(), name="messages_detail"),
    url(r'^messages/$', MessagesList.as_view(), name="messages_list"),
    url(r'^messages/sent/$', MessagesSent.as_view(), name="messages_sent"),
    url(r'^messages/new/$', MessageForm.as_view(), name="message_form"),
    url(r'^messages/reply/$', MessageReply.as_view(), name="message_reply"),