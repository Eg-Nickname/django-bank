from rest_framework import serializers
from transactions.models import Transaction
from account.models import Account


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_id', 'sender_id', 'reciver_id', 'kwota', 'waluta', 'data_transakcji', 'typ', 'title')

class SendTransactionSerializer(serializers.ModelSerializer):
    kwota = serializers.IntegerField(min_value=1, required=True)
    class Meta:
        model = Transaction
        fields = ('reciver_id', 'kwota', 'waluta', 'title')
    
    def validate(self, data):
        sender = self.context.get("request").user
        if sender == data['reciver_id']:
            raise serializers.ValidationError("You cannot send transaction to yourself.")
        if (getattr(sender, data['waluta'].lower()) - data['kwota']) < 0:
            raise serializers.ValidationError("Not enough founds.")

        print((getattr(sender, data['waluta'].lower()) - data['kwota']))
        return data

    def create(self, validated_data):
        sender = self.context.get("request").user
        reciver = validated_data['reciver_id']
        NewTransaction = Transaction(sender_id=sender, reciver_id=reciver, kwota=validated_data['kwota'], waluta=validated_data['waluta'], title=validated_data['title'])
        
        setattr(sender, validated_data['waluta'].lower(), getattr(sender, validated_data['waluta'].lower()) - validated_data['kwota'])
        setattr(reciver, validated_data['waluta'].lower(), getattr(reciver, validated_data['waluta'].lower()) + validated_data['kwota'])

        sender.save()
        reciver.save() 
        NewTransaction.save()

        return NewTransaction