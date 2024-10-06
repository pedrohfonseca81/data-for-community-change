export const useAppStore = defineStore('websiteStore', {
    state() {
        return {
            isLoading: true,
        }
    },
    actions: {
        setLoading(value: boolean) {
            this.isLoading = value;
        }
    }
});