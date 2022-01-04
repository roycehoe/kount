<script lang="ts" setup>
import { onBeforeMount, ref } from "vue";
import { ErrorCode, ErrorMsg } from "@/services/errors";
import { getQRResponse, QRResponse } from "@/services/QR/getQRResponse";
import { CreateQRForm, CreateQRResponse, getCreateQRResponse } from "@/services/QR/getCreateQRResponse";

const QRCodes = ref({} as QRResponse)
const QRImage = ref("")
const createQRForm = ref({} as CreateQRForm)

async function showQRCodes() {
  const { ok: isSuccessful, val: response } = await getQRResponse()
  if (isSuccessful) {
    QRCodes.value = response as QRResponse
  }
}

async function createQR() {
  const { ok: isSuccessful, val: response } = await getCreateQRResponse(createQRForm.value)
  if (isSuccessful) {
    const createQRResponse = response as CreateQRResponse
    QRImage.value = createQRResponse.QR_image
  }
}

onBeforeMount(async () => await showQRCodes());

</script>

<template>
  <link
    rel="stylesheet"
    href="https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined"
  />
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap"
    rel="stylesheet"
  />

  <div class="create-QR">
    <form @submit.prevent="createQR()" class="create-QR__form">
      <div class="create-QR__form--input">
        <it-input v-model="createQRForm.QR_data" placeholder="URL" />
        <it-input v-model="createQRForm.QR_size" placeholder="URL" />
      </div>
      <it-button class="create-QR__form--btn" type="success" outlined>Create QR</it-button>
    </form>
    <div class="create-QR__img">
      <img class="create-QR__img--small" src="../assets/graphics/logo.png" />
    </div>

    <it-divider />

    <it-collapse>
      <it-collapse-item title="My QR Codes">
        <div class="view-QR--space-between">
          <p class="view-QR__link--center">LINK GOES HERE</p>
          <it-dropdown>
            <it-button>...</it-button>
            <template #menu>
              <it-dropdown-menu slot="menu">
                <it-dropdown-item class="view-QR__btn--hover-red">Delete</it-dropdown-item>
              </it-dropdown-menu>
            </template>
          </it-dropdown>
        </div>
      </it-collapse-item>
    </it-collapse>
  </div>
  <p>{{ QRCodes }}</p>
  <p>QR Image:{{ QRImage }}</p>
</template>

<style scoped lang="scss">
.create-QR {
  margin-top: 10vh;
  margin-left: 10vw;
  margin-right: 10vw;
  &__form {
    display: flex;
    flex-direction: row;
    &--input {
      width: 100%;
      margin-right: 10px;
    }
    &--btn {
      width: 10%;
      // width: 100%;
    }
  }
  &__img {
    margin-top: 2vh;
    display: flex;
    justify-content: center;
    &--small {
      width: 300px;
      height: 100%;
    }
  }
}

.view-QR {
  &__link {
    &--center {
      display: flex;
      align-items: center;
    }
  }
  &--space-between {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  &__btn {
    &--hover-red {
      &:hover {
        background-color: #f93155;
      }
    }
  }
}

.test {
  padding: 0px;
}
</style>