from example_interfaces.srv import AddTwoInts
from k9_interfaces.srv import LtmRemember, LtmSetModel, LtmQuery

import rclpy
from rclpy.node import Node

class LongTermMemory(Node):

    def __init__(self):
        super().__init__('ltm_service')
        self.remember = self.create_service(LtmRemember, 'ltm_remember', self.ltm_remember_callback)
        self.query = self.create_service(LtmQuery, 'ltm_query', self.ltm_query_callback)
        self.set_model = self.create_service(LtmSetModel, 'ltm_set_model', self.ltm_set_model_callback)
  
    def ltm_remember_callback(self, request, response):
        #string<=512[<=20] up_to_twenty_topics_of_512_chars
        #---
        #bool success
        #uint8 facts_remembered
        response.success = True
        response.facts_remembered = len(request.up_to_twenty_topics_of_512_chars)
        self.get_logger().info(response.facts_remembered + " topics remembered.")
        return response
    
    def ltm_query_callback(self, request, response):
        #string query
        #---
        #bool success
        #string answer
        response.success = True
        response.answer = "The meaning of life is 42."
        self.get_logger().info("Question:" + request.query + "Answer:" + response.answer)
        return response
    
    def ltm_set_model_callback(self, request, response):
        #uint8 MODEL_TYPE_GENERATE=0
        #uint8 MODEL_TYPE_EMBED=1
        #
        #uint8 model_type
        #string model_name
        #---
        #bool success
        response.success = True
        self.get_logger().info('Incoming request\nModel_type: %i Model name: %s' % (request.model_type, request.model_name))
        return response

def main():
    rclpy.init()
    ltm_service = LongTermMemory()
    rclpy.spin(ltm_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
