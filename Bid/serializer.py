from rest_framework import serializers
from .models import Bid
from .models import Commpetition

class BidInitSerializer(serializers.ModelSerializer):
    status = serializers.CharField(default = "active") 
    class Meta:
        model = Bid
        fields = ('title','description','initial_price','status')
class BidListSer(serializers.ModelSerializer):
    class Meta:
        model = Commpetition
        fields=('__all__')



class BidCommpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commpetition
        fields = ('final_price',)
    def save(self,request,*args, **kwargs):
        user_id = request.user.identification_number
        request.session['user_id'] = user_id
        bidder=Commpetition(
            bid_id=1,
            
            final_price=self.validated_data['final_price'],

            customer_ID= request.session['user_id']
        )
        bidder.save()
        return bidder
        

        
        
class BidWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commpetition
        fields = ('bid_id','customer_id')

class BidClosingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bid
        fields = ('status',)

