import "slices"

func containsDuplicate(nums []int) bool {
    /*
        Brute Force Way:
            - Sort the array nums
            - Then have a ref number
            - Create a for loop, if a is equals to ref, then return true
            - If we get to the end of the loop without returning true, then return false
            - If let of array is less than or equals to 1 return false
    */
    if len(nums) <= 1 {
        return false
    }

    slices.Sort(nums)
    for i := 1; i < len(nums); i++ {
        if nums[i] == nums[i-1] {
            return true
        }
    }

    return false
}