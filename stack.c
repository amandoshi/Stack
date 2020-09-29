#include <stdio.h>
#include <string.h>
#include <stdbool.h>

//Stack Data Structure
typedef struct urlStack
{
	char url[2084];
	struct urlStack* next;
}urlStack;

//URL Stack
urlStack URL_STACK;

//Function Declarations
void push(char* url);
char* peek(void);
void pop(void);

int main(void)
{
	char* urls[5] = { "www.Youtube.com", "www.Google.com", "www.Netflix.com", "www.Apple.com", "www.StackOverFlow.com" };

	for (int i = 0; i < 5; i++)
	{
		push(urls[i]);
		printf("\nPush: %s", peek());
	}

	for (int i = 0; i < 5; i++)
	{
		pop();
		printf("\nPop: %s", peek());
	}

	return 0;
}

void push(char* newUrl)
{
	if (strcmp(URL_STACK.url, "") == false)
	{
		strcpy_s(URL_STACK.url, strlen(newUrl)+1, newUrl);
	}
	else
	{
		//Declare temp. pointer
		urlStack* tmpPtr;
		do
		{
			tmpPtr = malloc(sizeof(urlStack));
			if (tmpPtr == NULL)
			{
				free(tmpPtr);
			}
		} while (tmpPtr == NULL);

		//Copy URL STACK into temp. pointer
		strcpy_s(tmpPtr->url, strlen(URL_STACK.url) + 1, URL_STACK.url);
		tmpPtr->next = URL_STACK.next;

		//Copy new URL into URL STACK
		strcpy_s(URL_STACK.url, strlen(newUrl) + 1, newUrl);

		//Copy temp. pointer into URL STACK
		URL_STACK.next = tmpPtr;
	}
}

char* peek(void)
{
	if (URL_STACK.next != NULL)
	{
		return URL_STACK.next->url;
	}
	return "";
}

void pop(void)
{
	if (URL_STACK.next == NULL)
	{
		//Clear URL
		strcpy_s(URL_STACK.url, strlen("") + 1, "");
	}
	else
	{
		//Copy URL STACK Ptr into temp. pointer
		urlStack* tmpPtr = URL_STACK.next;

		//Copy temp. pointer into URL STACK
		strcpy_s(URL_STACK.url, strlen(tmpPtr->url) + 1, tmpPtr->url);
		URL_STACK.next = tmpPtr->next;

		//Free temp. pointer
		free(tmpPtr);

	}
}