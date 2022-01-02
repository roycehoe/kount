<script lang="ts" setup>
import { ref } from "vue";
import { ErrorCode, ErrorMsg } from "@/services/errors";
import { CreateUserRequest, getCreateUserResponse } from "@/services/user/getCreateUserResponse";

const newUserForm = ref({} as CreateUserForm);
const errorDisplay = ref("");
const isLoading = ref(false)
const accountCreated = ref(false);

interface CreateUserForm extends CreateUserRequest {
  confirmPassword: string;
}

async function createAccount(): Promise<void> {
  isLoading.value = true
  if (newUserForm.value.password != newUserForm.value.confirmPassword) {
    errorDisplay.value = ErrorMsg.NON_MATCHING_PASSWORDS;
    isLoading.value = false
    return
  }
  const { ok: isSuccessful, val: response } = await getCreateUserResponse(
    newUserForm.value
  );
  if (isSuccessful) {
    accountCreated.value = true;
    isLoading.value = false
    return;
  }
  switch (response) {
    case ErrorCode.USERNAME_TAKEN:
      errorDisplay.value = ErrorMsg.USERNAME_TAKEN;
      break;
    default:
      errorDisplay.value = ErrorMsg.SOMETHING_WENT_WRONG;
  }
  isLoading.value = false
}

</script>

<template>
  <form class="create-account-form" v-if="!accountCreated" @submit.prevent="createAccount">
    <div class="create-account-form__input">
      <input
        class="create-account-form__input--username"
        type="text"
        v-model="newUserForm.username"
        placeholder="New Username"
        autocomplete="off"
        required="true"
        maxlength="20"
      />

      <input
        class="create-account-form__input--password"
        type="password"
        v-model="newUserForm.password"
        placeholder="Password"
        autocomplete="off"
        required="true"
        maxlength="20"
      />

      <input
        class="create-account-form__input--confirm-password"
        type="password"
        v-model="newUserForm.confirmPassword"
        placeholder="Confirm Password"
        autocomplete="off"
        required="true"
        maxlength="20"
      />
    </div>

    <div class="create-account-form__submission-error">
      <p class="create-account-form__submission-error--msg">{{ errorDisplay }}</p>
    </div>

    <div class="create-account-form__btn">
      <button v-if="!isLoading" class="createAccountForm__btn--green" type="submit">
        <p class="createAccountForm__btn__txt">Create Account</p>
      </button>

      <button v-else class="createAccountForm__btn--loading" type="submit">
        <p class="createAccountForm__btn__txt">Loading...</p>
      </button>
    </div>

    <button class="createAccountForm__btn--grey" @click="$router.push('/')" type="button">
      <p class="createAccountForm__btn__txt">Return to Main Menu</p>
    </button>
  </form>

  <div class="createAccountSuccess" v-else>
    <p class="createAccountSuccess__txt">Account successfully created</p>
    <button class="createAccountForm__btn--grey" @click="$router.push('/')" type="button">
      <p class="createAccountForm__btn__txt">Return to Main Menu</p>
    </button>
  </div>
</template>

<style scoped lang="scss">
</style>