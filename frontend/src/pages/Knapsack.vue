<template>
  <q-page>
    <div class="page-container flex column q-mt-xl q-mx-auto">
      <div class="flex justify-between items-center">
        <h5 class="text-h5">Knapsack</h5>

        <div class="flex items-center">
          <q-input
            v-model="capacity"
            label="Capacidade mochila"
            type="number"
            :error="!capacity"
          >
            <template v-slot:error
              >A capacidade da mochila é obrigatória</template
            >
          </q-input>

          <q-btn
            color="primary"
            label="Montar mochila"
            class="q-ml-xl"
            style="height: 48px"
            @click="setKnapsack"
          />
        </div>
      </div>

      <div class="flex justify-between items-start">
        <div class="flex column items-container">
          <div class="flex wrap">
            <Item :item="item" :key="item.name" v-for="item in items" />
          </div>

          <div class="flex column q-mt-lg">
            <span class="text-subtitle1">
              <strong>Valor total:</strong> {{ calcTotalByKey(items, 'value') }}
            </span>

            <span class="text-subtitle1">
              <strong>Peso total:</strong> {{ calcTotalByKey(items, 'weight') }}
            </span>
          </div>
        </div>

        <div class="flex column items-container">
          <div class="flex wrap">
            <!-- eslint-disable-next-line vue/valid-v-for -->
            <!-- eslint-disable-next-line prettier/prettier -->
            <Item :item="item" :key="`selected-${idx}`" v-for="(item, idx) in selectedItems" />
          </div>

          <div class="flex column q-mt-lg">
            <span class="text-subtitle1">
              <strong>Valor total:</strong>
              {{ calcTotalByKey(selectedItems, 'value') }}
            </span>

            <span class="text-subtitle1">
              <strong>Peso total:</strong>
              {{ calcTotalByKey(selectedItems, 'weight') }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<style>
.page-container {
  width: 80%;
}

.items-container {
  width: 45%;
  max-width: 400px;
}
</style>

<script>
import { mapGetters } from 'vuex';
import Item from 'src/components/Item.vue';

export default {
  name: 'PageKnapsack',
  components: { Item },
  created() {
    this.selectedItems = new Array(this.items.length).fill(null);
  },
  computed: mapGetters({
    items: 'app/items',
  }),
  data() {
    return {
      capacity: 170,
      selectedItems: [],
    };
  },
  methods: {
    setKnapsack() {
      console.log('opa');
    },
    calcTotalByKey(list, key) {
      let sum = 0;

      list.forEach((item) => {
        sum += parseFloat(item ? item[key] : 0);
      });

      return Math.round(sum * 100) / 100;
    },
  },
};
</script>
