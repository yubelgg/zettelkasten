// JoinExample.java
public class JoinExample extends Thread {
    private int threadNumber;

    public JoinExample(int threadNumber) {
        this.threadNumber = threadNumber;
    }

    @Override
    public void run() {
        System.out.println("Thread " + threadNumber + " is starting.");
        System.out.println("Thread " + threadNumber + " has finished.");
    }

    public static void main(String[] args) {
        JoinExample thread1 = new JoinExample(1);
        JoinExample thread2 = new JoinExample(2);
        JoinExample thread3 = new JoinExample(3);

        thread1.start();
        thread2.start();
        thread3.start();

        try {
            // Main thread waits for thread1 to finish
            // thread1.join();
            System.out.println("Main thread: Thread 1 has completed.");

            // Then waits for thread2 to finish
            // thread2.join();
            System.out.println("Main thread: Thread 2 has completed.");

            // Finally waits for thread3 to finish
            thread3.join();
            System.out.println("Main thread: Thread 3 has completed.");
        } catch (InterruptedException e) {
            System.out.println("Main thread was interrupted.");
        }

        System.out.println("Main thread has finished execution.");
    }
}
