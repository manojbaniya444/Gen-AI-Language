from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class PersonIntel(BaseModel):
    summary:str = Field(subscription="Summary of a person")
    facts:list = Field(subscription="Interesting facts about a person")
    topics_of_interest:list = Field(subscription="Topics of interest of a person")
    ice_breaker:str = Field(subscription="Create ice breaker to open a conversation with a person")
    
    
    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breaker": self.ice_breaker
        }
        
person_intel_parser = PydanticOutputParser(pydantic_object=PersonIntel)