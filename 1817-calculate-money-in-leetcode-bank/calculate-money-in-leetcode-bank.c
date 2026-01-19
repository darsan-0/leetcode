int totalMoney(int n) {
    int total = 0;
    int start = 1;   // Monday starting deposit

    for (int i = 0; i < n; i++) {
        total = total + start + (i % 7);

        // After Sunday, next Monday increases by 1
        if (i % 7 == 6) {
            start++;
        }
    }

    return total;
}
