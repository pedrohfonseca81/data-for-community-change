export const useAppStore = defineStore('websiteStore', {
    state() {
        return {
            isLoading: true,
            filters: {
                flooding: false,
                temperature: true,
                storm: false,
                landslides: false,
                forestFire: false,
            }
        }
    },
    actions: {
        setLoading(value: boolean) {
            this.isLoading = value;
        },
        setFilter(key: keyof typeof this.filters, value: boolean) {
            this.filters[key] = value;
        },
    }
});