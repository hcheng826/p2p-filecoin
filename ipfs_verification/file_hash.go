package main

import (
	"bufio"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"log"
	"math/rand"
	"os"
	"time"
)

func readFile(filename string) []byte {
	f, err := os.Open(filename)
	if err != nil {
		return nil
	}
	defer f.Close()

	stats, statsErr := f.Stat()
	if statsErr != nil {
		return nil
	}

	var size = stats.Size()
	bytes := make([]byte, size)

	bufr := bufio.NewReader(f)
	_, err = bufr.Read(bytes)

	if err != nil {
		return nil
	}

	return bytes
}

func genRandomString(length int) string {
	var hexRunes = []rune("abcdef0123456789")
	b := make([]rune, length)
	for i := range b {
		b[i] = hexRunes[rand.Intn(len(hexRunes))]
	}
	return string(b)
}

func hexToBytes(hexstr string) []byte {
	src := []byte(hexstr)
	dst := make([]byte, hex.DecodedLen(len(src)))
	n, err := hex.Decode(dst, src)
	if err != nil {
		log.Fatal(err)
	}
	return dst[:n]
}

func getSHA256(bytes []byte) []byte {
	H := sha256.New()
	H.Write(bytes)
	return H.Sum(nil)
}

func initSeed() {
	rand.Seed(time.Now().UnixNano())
}

func getToken() (string, []byte) {
	token := genRandomString(32)
	return token, hexToBytes(token)
}

func main() {
	// initSeed()
	// token, tokenBytes := getToken()
	// fmt.Printf("Token:\n  %s\n", token)
	tokenBytes := os.Args[2]

    filepath := os.Args[1]
	// fileData := readFile("file_check.go")
    // fmt.Printf("%s\n", filepath)
	fileData := readFile(filepath)
	// fmt.Printf("Hash of original file:\n  %x\n", getSHA256(fileData))

	fileDataConcat := append(fileData, tokenBytes...)
	// fmt.Printf("Hash of concatenated file:\n  %x\n", getSHA256(fileDataConcat))
	fmt.Printf("%x", getSHA256(fileDataConcat))
}
