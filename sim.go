package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
)

// Roll a die until first is hit, immediately followed by second
// Return the number of rolls to end the game
// x and y must be in {min,...,max}
func playGame(first int, second int, min int, max int) int {
	last := -1
	for nRolls := 1; ; nRolls++ {
		roll := rand.Intn(max) + min
		if last == first && roll == second {
			return nRolls
		}
		last = roll
	}
}

// Play the game with a six-sided die
func playDieGame(first int, second int) int {
	return playGame(first, second, 1, 6)
}

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Usage: go run sim.go nTrials\n")
		os.Exit(1)
	}

	nTrials, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(1)
	}

	fiveSixRolls := 0
	fiveFiveRolls := 0

	for n := 0; n < nTrials; n++ {
		fiveSixRolls += playDieGame(5, 6)
		fiveFiveRolls += playDieGame(5, 5)
	}

	fmt.Printf("Five-Six game average rolls: %v\n", fiveSixRolls/nTrials)
	fmt.Printf("Five-Five game average rolls: %v\n", fiveFiveRolls/nTrials)
}
