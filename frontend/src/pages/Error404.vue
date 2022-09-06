<template>
  <div
    class="fullscreen bg-primary text-white text-center q-pa-md flex flex-center"
  >
    <div>
      <div style="font-size: 30vh">404</div>

      <div class="text-h2" style="opacity: 0.4">Oops. Nada aqui...</div>

      <q-btn
        class="q-mt-xl"
        color="accent"
        text-color="white"
        unelevated
        to="/"
        label="Ir para Home"
        no-caps
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ErrorNotFound',
};
</script>
