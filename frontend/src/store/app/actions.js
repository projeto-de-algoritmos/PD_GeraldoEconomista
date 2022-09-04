export const addItem = ({ commit, rootState }, item) => {
  const { items } = rootState.app;

  const newItems = [...items, item];

  commit('setItems', newItems);
};

export const removeItem = ({ commit, rootState }, itemId) => {
  const { items } = rootState.app;

  const newItems = [...items];

  const idx = newItems.findIndex((item) => item.id === itemId);

  if (idx < 0) return;

  newItems.splice(idx, 1);

  commit('setItems', newItems);
};

export const editItem = ({ commit, rootState }, { itemId, data }) => {
  const { items } = rootState.app;

  const newItems = [...items];

  const idx = newItems.findIndex((item) => item.id === itemId);

  if (idx < 0) return;

  newItems[idx] = { ...newItems[idx], ...data };

  commit('setItems', newItems);
};

export const getItem = ({ rootState }, itemId) => {
  const { items } = rootState.app;

  return items.find((item) => item.id === itemId);
};

export const deleteAll = ({ commit }) => {
  commit('setItems', []);
};
