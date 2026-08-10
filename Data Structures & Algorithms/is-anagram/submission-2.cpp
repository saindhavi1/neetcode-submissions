class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> characterCount;

        if (s.size() != t.size()){
            return false;
        }
        for (int i = 0; i < s.size(); i++) {
            characterCount[s[i]]++;
        }

        for (int j = 0; j < t.size(); j++) {
            characterCount[t[j]]--;
        }

        for (int k = 0; k < s.size(); k++){
            if (characterCount[s[k]] != 0){
                return false;
            }
        }
        return true;
    }
};