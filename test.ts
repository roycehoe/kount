enum questionTypes {
    Text = "TEXT",
    MultipleChoice = "MULTIPLECHOICE"
}


interface SurveyQuestion {
    type: questionTypes
    title: string
    options?: Array<string>
}

interface SurveyQuestionForm {
    surveyQuestions: Array<SurveyQuestion>
}

const mock = {
    surveyQuestions: [{
        type: questionTypes.Text,
        title: "Y R U GEH"
    },
    {
        type: questionTypes.MultipleChoice,
        title: "WHAT IS YOUR GEH LEVEL?",
        options: ["1", "2", "3", "4"]
    }
    ]
} as SurveyQuestionForm
