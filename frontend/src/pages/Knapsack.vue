<template>
  <q-page>
    <q-stepper
      v-model="step"
      animated
      header-nav
      ref="stepper"
      color="primary"
      class="page-container q-mt-lg q-mx-auto no-shadow"
    >
      <q-step
        :name="1"
        title="Selecionar itens disponíveis"
        icon="list"
        :done="done1"
      >
        <q-table
          title="Itens"
          :data="items"
          row-key="name"
          :columns="columns"
          selection="multiple"
          :selected.sync="selectedItems"
          :pagination.sync="pagination"
          no-data-label="Nenhum item cadastrada"
        >
          <template v-slot:top>
            <div class="flex column">
              <span class="text-h5 q-my-md">Itens</span>

              <span class="text-body2">
                Selecione os itens disponíveis, estes serão utilizados para
                montar a mochila
              </span>
            </div>
          </template>

          <template v-slot:body-cell-imageUrl="props">
            <q-td :props="props">
              <q-img
                style="width: 32px; height: 32px"
                :src="props.row.imageUrl"
              />
            </q-td>
          </template>

          <template v-slot:no-data="{ icon, message }">
            <div
              class="full-width row flex-center q-gutter-sm"
              style="color: #ff00ff"
            >
              <q-icon size="2em" name="sentiment_dissatisfied" />

              <span> {{ message }} </span>

              <q-icon size="2em" :name="icon" />
            </div>
          </template>
        </q-table>

        <q-stepper-navigation align="right">
          <q-btn
            @click="
              () => {
                knapsackItems = new Array(selectedItems.length).fill(null);
                done1 = true;
                step = 2;
              }
            "
            color="primary"
            label="Próximo"
          />
        </q-stepper-navigation>
      </q-step>

      <q-step
        :name="2"
        title="Montar mochila com os itens selecionados"
        icon="backpack"
        :done="done2"
      >
        Defina a capacidade da mochila e clique em "Montar Mochila"

        <div class="flex column">
          <div class="flex justify-between items-center">
            <h5 class="text-h5">Knapsack</h5>

            <div class="flex items-center">
              <q-input
                v-model="capacity"
                label="Capacidade mochila (g)"
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

          <div class="flex justify-between">
            <div class="flex column items-container">
              <div class="flex wrap">
                <Item
                  :item="item"
                  :key="item.name"
                  v-for="item in selectedItems"
                />
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

            <div class="flex column items-container">
              <div class="flex wrap">
                <!-- eslint-disable-next-line vue/valid-v-for -->
                <!-- eslint-disable-next-line prettier/prettier -->
                <Item :item="item" :key="`selected-${idx}`" v-for="(item, idx) in knapsackItems" />
              </div>

              <div class="flex column q-mt-lg">
                <span class="text-subtitle1">
                  <strong>Valor total:</strong>
                  {{ knapsackTotalValue }}
                </span>

                <span class="text-subtitle1">
                  <strong>Peso total:</strong>
                  {{ knapsackTotalWeight }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <q-stepper-navigation class="q-pa-none">
          <q-btn @click="step = 1" color="primary" label="Back" />
        </q-stepper-navigation>
      </q-step>
    </q-stepper>
  </q-page>
</template>

<style>
.page-container {
  width: 80%;
}

.items-container {
  width: 45%;
  height: fit-content;
  max-width: 400px;
}
</style>

<script>
import { mapActions, mapGetters } from 'vuex';
import Item from 'src/components/Item.vue';

import { assembleKnapsack } from 'src/store/app/actions';

export default {
  name: 'PageKnapsack',
  components: { Item },
  created() {
    this.fetchItems().then(() => {
      this.selectedItems = [...this.items];
      this.knapsackItems = new Array(this.items.length).fill(null);
    });
  },
  mounted() {
    this.$q.lang.table.recordsPerPage = 'Registros por páginas';

    this.$q.lang.table.pagination = (start, end, total) => {
      return `${start}-${end} de ${total}`;
    };

    this.$q.lang.table.selectedRecords = (rows) => {
      return rows === 1
        ? '1 registro selecionado.'
        : `${rows === 0 ? 'Nenhum' : rows} registro(s) selecionado(s).`;
    };
  },
  computed: mapGetters({
    items: 'app/items',
  }),
  data() {
    return {
      step: 1,
      done1: false,
      done2: false,
      capacity: 170,
      knapsackTotalValue: 0,
      knapsackTotalWeight: 0,
      knapsackItems: [],
      selectedItems: [],
      pagination: {
        rowsPerPage: 15,
      },
      columns: [
        {
          name: 'name',
          label: 'Nome',
          align: 'left',
          required: true,
          field: 'name',
        },
        {
          name: 'value',
          label: 'Valor',
          align: 'left',
          required: true,
          field: 'value',
          format: (val) => `${val} orens`,
        },
        {
          name: 'weight',
          label: 'Peso',
          align: 'left',
          required: true,
          field: 'weight',
          format: (val) => `${val} g`,
        },
        {
          name: 'imageUrl',
          label: 'Imagem',
          align: 'left',
          required: true,
          field: 'imageUrl',
        },
      ],
    };
  },
  methods: {
    ...mapActions({
      fetchItems: 'app/getItems',
    }),
    setKnapsack() {
      assembleKnapsack({
        capacity: parseInt(this.capacity, 10),
        items: this.selectedItems.map(({ name }) => ({ name, quantity: 1 })),
      }).then((data) => {
        const diff = Math.abs(data.solution.length - this.selectedItems.length);

        this.knapsackItems = [
          ...data.solution,
          ...(diff > 0 ? new Array(diff).fill(null) : []),
        ];
        this.knapsackTotalValue = data.result;
        this.knapsackTotalWeight = data.weight;
      });
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
