from django.urls import path
# from .views import CreateBid
from .views import BidWinner
from .views import BidInitialization,BidCommpitionInfo
urlpatterns = [
    path('BidCommpitionInfo', BidCommpitionInfo.as_view()),
    path('BidInitialization',BidInitialization.as_view()),
    path('winner',BidWinner.as_view()),

    # path('<str:pk>', Bid.as_view())
]