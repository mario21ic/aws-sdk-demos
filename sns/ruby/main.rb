require 'aws-sdk'

sns = Aws::SNS::Client.new(region: 'us-west-2', access_key_id: 'ACCESS_KEY_ID', secret_access_key: 'SECRET_ACCESS_KEY')
message_id = sns.publish(phone_number: '+51966696636', message: 'Testing message')
puts message_id


