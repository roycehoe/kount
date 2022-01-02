<script lang="ts" setup>
import { ref } from "vue";
import router from "@/router";
import { ErrorCode, ErrorMsg } from "@/services/errors";
import { AuthUserRequest, AuthUserResponse, getAuthUserResponse } from "@/services/user/getAuthUserResponse";

const loginForm = ref({} as AuthUserRequest);
const errorDisplay = ref("");
const isLoading = ref(false)

async function login(): Promise<void> {
  errorDisplay.value = ""
  isLoading.value = true
  const { ok: isSuccessful, val: response } = await getAuthUserResponse(
    loginForm.value
  );

  if (isSuccessful) {
    const { access_token: token } = response as AuthUserResponse;
    localStorage.removeItem("token");
    localStorage.setItem("token", token);
    router.push({
      path: '/play',
    })
    return;
  }
  switch (response) {
    case ErrorCode.INVALID_CREDENTIALS:
      errorDisplay.value = ErrorMsg.INVALID_CREDENTIALS;
      break;
    default:
      errorDisplay.value = ErrorMsg.SOMETHING_WENT_WRONG;
  }
  isLoading.value = false
}
</script>

<template>
  <div class="login-display">
    <form class="login-form" @submit.prevent="login">
      <div class="login-form__username">
        <input
          class="login-form__username--grey-input"
          type="text"
          v-model="loginForm.username"
          placeholder="Username"
          autocomplete="off"
          maxlength="20"
          required="true"
        />
      </div>

      <div class="login-form__password">
        <input
          class="login-form__password login-form__password--input"
          type="password"
          v-model="loginForm.password"
          placeholder="Password"
          autocomplete="off"
          maxlength="20"
          required="true"
        />
      </div>
      <div class="login-box__credentials-error">
        <p class="login-box__credentials-error--msg">{{ errorDisplay }}</p>
      </div>

      <div class="login-form__loginButton">
        <button v-if="!isLoading" class="login-form__login-button--greenButton" type="submit">Log in</button>
        <button v-else class="login-form__login-button--loading" disabled>Loading...</button>
      </div>
    </form>

    <div class="create-account">
      <div class="create-account__question">
        <p class="create-account__question--txt">Don't have an account yet?</p>
      </div>

      <div class="create-account__link">
        <router-link class="create-account__link--txt" to="/new">Create an account</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>