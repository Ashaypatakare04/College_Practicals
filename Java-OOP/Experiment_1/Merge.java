public class Merge {
    public static void main(String[] args) {

        int arr1[] = {1,2,3,4,5};
        int arr2[] = {6,7,8,9, 10};

        // create new array
        int arr3[] = new int[arr1.length + arr2.length];

        // copy arr1 into arr3
        for (int i = 0; i < arr1.length; i++) {
            arr3[i] = arr1[i];
        }

        // copy arr2 into arr3
        for (int i = 0; i < arr2.length; i++) {
            arr3[arr1.length + i] = arr2[i];
        }

        // print merged array
        System.out.println("Merged Array:");
        for (int i = 0; i < arr3.length; i++) {
            System.out.print(arr3[i] + " ");
        }
    }
}

