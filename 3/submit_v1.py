class Solution(object):
    def lengthOfLongestSubstring(self, s):
        def has_duplicate_str(st):
            cnt = 0
            for i in range(0, len(st), 1):
                cnt += st.count(st[i])

            if cnt != len(st):
                return True
            else:
                return False


        def trim_same_strings(s):
            s_copy = s
            start_str = s[0]
            end_str = s[-1]

            for i in range(1, len(s_copy), 1):
                if s[i] == start_str:
                    s_copy = s_copy[1:]
                else:
                    break

            for i in range(-2, -len(s_copy) - 1, -1):
                if s[i] == end_str:
                    s_copy = s_copy[:-1]
                else:
                    break

            return s_copy


        longest_substr = ""
        substr = s
        p_skip = []

        if len(s) == 0:  # ex. None
            return 0

        # trim repeated string at back and end
        # aaa -> a
        # qq -> q

        s = trim_same_strings(s)

        if (len(s) == 2) and (s[0] != s[1]):  # ex. ab
            longest_substr = s

        if s.count(s[0]) == len(s):  # ex. bbbbbbbbbbbbb
            return 1

        longest_substr = s[0:2]

        start_time = time.time()
        jump = 1
        for p in range(0, len(s), 1):
            if len(longest_substr) > (len(s) - p):
                break
            if p in p_skip:
                continue

            for q in range(0, len(s), jump):
                if p >= q:  # [0:0], [1:1] / [1:0], [3:1] is meaningless
                    continue
                # print(p, q)
                if len(longest_substr) <= len(substr[p: q + 2]):  # when new substr is longer than pre-substring (longest_substring
                    try:
                        if substr[q + 1] in substr[p: q + 1]:  # ex: abcabc / p == 0, q == 3, abc, a(index 3) is in abc, skip to p == 3 index(3), skipping 0, 1, 2, q = 2
                            break

                        elif substr[q + 1] not in substr[p: q + 1]:  # upcoming string is not in subtring
                            if has_duplicate_str(substr[p: q + 1]):  # if substring got cut wrongly
                                continue

                            if len(substr[p: q + 2]) == len(longest_substr):  # if length is same, no need to reassign value
                                continue

                            longest_substr = substr[p: q + 2]
                            if len(s) >= 30000:
                                jump = len(longest_substr)
                    except:
                        continue
                else:
                    continue

        longest_substr = trim_same_strings(longest_substr)

        # print(longest_substr, len(longest_substr))
        return len(longest_substr)