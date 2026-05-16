from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5.4-mini",
    temperature=0.5
)

template = """
너는 조사병단을 이끄는 리바이 병장이다.
지금은 임시적으로 기상캐스터 역할을 맡고 있으며,
리바이 특유의 냉정하고 직설적인 말투로 날씨를 전달한다.

반드시 슬랙 메시지에 바로 붙여넣을 수 있는 형태로 출력해라.

규칙:
- 슬랙 마크다운 문법을 사용한다.
- 강조할 문장은 반드시 *이렇게* 감싼다. (** 사용 금지)
- 줄바꿈을 자연스럽게 넣어서 가독성을 높여라.
- 필요하면 짧게 압박하거나 경고하는 말투를 사용해도 된다.
- 날씨 정보를 단순 나열하지 말고 상황을 해석해서 말해라.
- 마지막에는 전체 날씨를 한 줄로 정리해라.
- 이모지는 사용하지 않는다.
- 출력은 멘트만 생성하고 설명은 하지 않는다.

내일 날씨 정보

오전 날씨: {morning_weather}
오전 강수확률: {morning_rain}

오후 날씨: {afternoon_weather}
오후 강수확률: {afternoon_rain}

최저 기온: {lowest_temp}
최고 기온: {highest_temp}
"""

prompt = PromptTemplate.from_template(template)
outputparser = StrOutputParser()
chain = prompt | llm | outputparser

def weather_forecast(morning_weather, morning_rain, afternoon_rain, afternoon_weather, lowest_temp, highest_temp):



    respond = chain.invoke({"morning_weather" : morning_weather, 
                        "morning_rain" : morning_rain,
                        "afternoon_weather" : afternoon_weather,
                        "afternoon_rain" : afternoon_rain,
                        "lowest_temp" : lowest_temp,
                        "highest_temp" : highest_temp
    })
    message = "<!channel>\n" + respond 
    return message