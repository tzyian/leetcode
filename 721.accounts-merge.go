package leetcode

import "slices"

// @leet start

type user struct {
	emails map[string]struct{}
	name   string
}

// Doing one by one wouldn't work because A(1, 2) and B(3, 4) but C(2,3), so need to recursively merge all
func accountsMerge(accounts [][]string) [][]string {
	userEmails := make(map[string]*user)
	userList := make([]*user, 0)

	for _, acc := range accounts {
		newUser := &user{emails: make(map[string]struct{})}
		existingUser := &user{}
		existingFound := false

		for i, ele := range acc {
			if i == 0 { // Name
				newUser.name = ele
			} else { // Emails
				newUser.emails[ele] = struct{}{}
				usr, ok := userEmails[ele]
				if !ok {
					userEmails[ele] = newUser
				} else {
					existingFound = true
					existingUser = usr
				}
			}

			if existingFound {
				merge(existingUser, newUser)
			} else {
				userList = append(userList, newUser)
			}
		}
	}

	ans := make([][]string, len(userList))
	for i, usr := range userList {
		accountDetails := make([]string, len(usr.emails))
		count := 0
		for k, _ := range usr.emails {
			accountDetails[count] = k
			count++
		}
		slices.Sort(accountDetails)
		accountDetails = append([]string{usr.name}, accountDetails...)
		ans[i] = accountDetails
	}

	return ans

}

func merge(keepUser, delUser *user) *user {
	for k, _ := range delUser.emails {
		keepUser.emails[k] = struct{}{}
	}
	return keepUser

}

// @leet end
