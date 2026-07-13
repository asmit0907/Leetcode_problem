import java.util.HashMap;
import java.util.HashSet;

class Solution { 
    public String mostCommonWord(String paragraph, String[] banned) { 
        HashSet<String> bannedSet = new HashSet<>();
        for (String w : banned) {
            bannedSet.add(w);
        }
        
        HashMap<String, Integer> counts = new HashMap<>();
        String mostCommon = "";
        int maxCount = 0;
        
        StringBuilder currentWord = new StringBuilder();
        String standardText = paragraph.toLowerCase() + " "; 
        
        for (int i = 0; i < standardText.length(); i++) {
            char c = standardText.charAt(i);
            
            if (c >= 'a' && c <= 'z') {
                currentWord.append(c);
            } else {
                String word = currentWord.toString();
                
                if (word.length() > 0 && !bannedSet.contains(word)) {
                    int currentCount = 1;
                    if (counts.containsKey(word)) {
                        currentCount = counts.get(word) + 1;
                    }
                    counts.put(word, currentCount);
                    
                    if (currentCount > maxCount) {
                        maxCount = currentCount;
                        mostCommon = word;
                    }
                }
                currentWord.setLength(0);
            }
        }
        
        return mostCommon;
    } 
}