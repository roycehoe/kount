<script lang="ts" setup>
import SurveyList from '@/components/SurveyList.vue';
import { onBeforeMount, ref } from 'vue';
import SurveyCreateMenu from '@/components/SurveyCreateMenu.vue';
import { getSurveyQuestions } from '@/services/survey/getSurveyQuestions';
import { CreateSurveyResponse } from '@/services/survey/getCreateSurveyResponse';


interface surveyQuestionResponse {
  question: string
  answer: string
}

const surveyId = 4
const surveyQuestionsDisplay = ref({} as CreateSurveyResponse)
const surveyFormResponse = ref([] as Array<surveyQuestionResponse>)





async function showSurveyQuestions(surveyId: number) {
  const { ok: isSuccessful, val: response } = await getSurveyQuestions(surveyId)
  if (isSuccessful) {
    surveyQuestionsDisplay.value = response as CreateSurveyResponse
  }
  //to implement error handling
}

onBeforeMount(async () => await showSurveyQuestions(surveyId));

</script>

<template>
  <div class="bg-white shadow">
    <div class="ml-16 py-6 px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-gray-900">{{ surveyQuestionsDisplay.title }}</h1>
    </div>
  </div>

  <div class="m-24">
    <div class="form-control my-6" v-for="question in surveyQuestionsDisplay.questions">
      <label class="label">
        <span class="label-text font-bold">{{ question }}</span>
      </label>
      <input type="text" placeholder="answer" class="input input-accent input-bordered" />
    </div>
    <button class="btn btn-success">Submit</button>
  </div>
  <p>{{ surveyFormAnswers }}</p>
</template>

<style scoped lang="scss">
</style>